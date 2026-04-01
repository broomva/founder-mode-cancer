# End-to-End Test Plan: Founder-Mode Oncology Pipeline

## Scenario

Run the full personalized oncology pipeline on Sid Sijbrandij's publicly available osteosarcoma data — from raw sequencing through neoantigen prediction to AlphaFold structural validation — producing a ranked vaccine candidate list and treatment recommendation.

**Primary data source**: `gs://osteosarc-genomics` (24.88 TiB, publicly readable)

---

## Phase 1: Data Acquisition (~20 GB download)

**Use the pre-called variants + existing RNA-seq** to skip the compute-heavy alignment step.

| Data | Source Path | Size |
|------|-----------|------|
| Somatic VCFs (Sarek 3.5.1) | `gs://osteosarc-genomics/genomics_reprocessing/DNA/T2_2025_01_WGS_sarek_variants/` | ~2 GB |
| Bulk RNA-seq BAMs | `gs://osteosarc-genomics/rna-seq/` | ~10 GB |
| scRNA-seq (tumor T1, Seurat RDS) | `gs://osteosarc-genomics/ucsf/T1/` | ~5 GB |
| HLA typing | osteosarc.com data page | Metadata |
| Neoantigen predictions (existing) | `gs://osteosarc-genomics/neoantigen_prediction/` | 178 MB |

```bash
mkdir -p data/{variants,rnaseq,scrna,hla,neoantigens,reference}

# Pre-called variants (Mutect2, Strelka, FreeBayes from Sarek)
gsutil -m cp -r gs://osteosarc-genomics/genomics_reprocessing/DNA/T2_2025_01_WGS_sarek_variants/ data/variants/

# Bulk RNA-seq
gsutil -m cp gs://osteosarc-genomics/rna-seq/fastq/tumor_T1* data/rnaseq/

# scRNA-seq (processed Seurat objects for speed)
gsutil -m cp gs://osteosarc-genomics/ucsf/T1/*.rds data/scrna/

# Existing neoantigen predictions (for validation)
gsutil -m cp -r gs://osteosarc-genomics/neoantigen_prediction/ data/neoantigens/
```

**Fallback** (if osteosarc.com paths differ): Use GSE152048 from GEO for scRNA-seq (100K osteosarcoma cells, direct download).

**Success criteria**: VCFs + RNA-seq + scRNA-seq + HLA alleles all available locally.

---

## Phase 2: Variant Annotation (1-2 hours)

Since osteosarc.com provides pre-called VCFs from Sarek (Mutect2 + Strelka + FreeBayes), skip alignment and variant calling. Annotate for pVACseq.

```bash
# Install VEP
pip install ensembl-vep  # or conda install -c bioconda ensembl-vep

# Annotate VCF with VEP (required by pVACseq)
vep --input_file data/variants/mutect2_filtered.vcf.gz \
    --output_file results/variants/annotated.vcf \
    --format vcf --vcf \
    --symbol --terms SO --tsl --hgvs \
    --plugin Downstream --plugin Wildtype \
    --assembly GRCh38 --offline --fork 8 \
    --dir_cache data/reference/vep_cache/
```

**Success criteria**: VEP-annotated VCF with gene symbols, protein changes, and consequence annotations.

---

## Phase 3: scRNA-seq Target Discovery (2-4 hours)

Replicate the critical diagnostic insight: identify non-obvious surface targets.

```python
import scanpy as sc

# Load (Seurat RDS via rpy2, or use H5AD if available)
adata = sc.read_h5ad('data/scrna/tumor_T1.h5ad')
# OR convert from Seurat: SeuratDisk::Convert("data/scrna/tumor.rds", dest="h5ad")

# Standard pipeline
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=3000)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.8)

# TARGET DISCOVERY — the key step
targets = ['FAP', 'CD276', 'EPHA2', 'MSLN', 'FOLR1', 'MUC1', 'ERBB2', 'EGFR', 'MET']
sc.pl.dotplot(adata, targets, groupby='leiden', save='_target_discovery.pdf')
sc.tl.rank_genes_groups(adata, 'leiden', method='wilcoxon')
```

**Success criteria**: FAP overexpression confirmed in tumor clusters (log2FC > 1, padj < 0.05). Additional targets identified (B7H3, EphA2).

---

## Phase 4: Neoantigen Prediction (2-4 hours)

```bash
pip install pvactools mhcflurry vaxrank
mhcflurry-downloads fetch

# pVACseq — predict neoantigens
pvacseq run \
  results/variants/annotated.vcf \
  "sid_osteo" \
  "HLA-A*02:01,HLA-A*24:02,HLA-B*07:02,HLA-B*44:02,HLA-C*07:02,HLA-C*05:01" \
  MHCflurry MHCnuggetsI \
  results/neoantigens/ \
  -e1 8,9,10,11 \
  -t 16 \
  --binding-threshold 500

# Vaxrank — integrated ranking (binding + expression + VAF)
vaxrank \
  --vcf data/variants/mutect2_filtered.vcf.gz \
  --bam data/rnaseq/tumor_aligned.bam \
  --mhc-predictor mhcflurry \
  --mhc-alleles "HLA-A*02:01,HLA-A*24:02,HLA-B*07:02,HLA-B*44:02" \
  --output-xlsx-report results/neoantigens/vaxrank_report.xlsx

# Select top 50 for structural validation
python3 -c "
import pandas as pd
pvac = pd.read_csv('results/neoantigens/MHC_Class_I/sid_osteo.filtered.tsv', sep='\t')
top50 = pvac.nsmallest(50, 'Best MT IC50 Score')
top50.to_csv('results/neoantigens/top50_candidates.csv', index=False)
print(f'Top 50 candidates selected. Best IC50: {top50.iloc[0][\"Best MT IC50 Score\"]:.1f} nM')
"
```

**Validation**: Compare our predictions against the existing neoantigen predictions in `data/neoantigens/` from osteosarc.com and the vaccine neoantigen overlap spreadsheet.

**Success criteria**: 50+ candidates with IC50 < 500nM, expression confirmed, VAF > 5%.

---

## Phase 5: AlphaFold Structural Validation (4-12 GPU hours)

```python
# Prepare peptide-MHC FASTA pairs for AlphaFold Multimer
import pandas as pd

HLA_A0201 = "GSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQRMEPRAPWIEQEG..."  # full sequence

candidates = pd.read_csv('results/neoantigens/top50_candidates.csv')
for idx, row in candidates.iterrows():
    with open(f'results/alphafold/inputs/pair_{idx}.fasta', 'w') as f:
        f.write(f">peptide\n{row['MT Epitope Seq']}\n>HLA\n{HLA_A0201}\n")
```

```bash
# Run via Modal (recommended)
modal run modal_colabfold.py \
  --input-dir results/alphafold/inputs/ \
  --output-dir results/alphafold/outputs/ \
  --model-type alphafold2_multimer_v3

# OR via ColabFold locally
colabfold_batch results/alphafold/inputs/ results/alphafold/outputs/ \
  --model-type alphafold2_multimer_v3
```

```python
# Score and rank
import json, glob
results = []
for d in sorted(glob.glob('results/alphafold/outputs/pair_*')):
    ranking = json.load(open(f'{d}/ranking_debug.json'))
    best = ranking['order'][0]
    results.append({
        'idx': int(d.split('_')[-1]),
        'iptm': ranking['iptm'][best],
        'ptm': ranking['ptm'][best],
    })

af = pd.DataFrame(results)
af['pass'] = (af['iptm'] > 0.5)
af['tier'] = af.apply(lambda r: 'T1' if r['iptm'] > 0.6 else ('T2' if r['iptm'] > 0.5 else 'T3'), axis=1)

# Merge with sequence scores and produce final ranking
merged = candidates.merge(af, left_index=True, right_on='idx')
final = merged[merged['pass']].sort_values('iptm', ascending=False)
final.to_csv('results/FINAL_neoantigen_candidates_ranked.csv', index=False)
```

**Success criteria**: 5+ candidates pass structural validation (ipTM > 0.5). At least 2 at T1 tier.

---

## Phase 6: Treatment Recommendation

Apply the skill's decision workflow to compile a full treatment plan using findings from Phases 2-5.

**Output**: `results/TREATMENT_RECOMMENDATION.md` containing:
- Diagnostic summary (mutations, targets, HLA, immune landscape)
- 5-layer treatment combination (checkpoint + vaccine + oncolytic + cell therapy + radioligand)
- Regulatory access pathway per agent (Form 3926 timelines)
- Monitoring protocol (ctDNA every 2 weeks, scRNA-seq monthly, PET quarterly)
- Maintenance plan (mRNA vaccine updates, ctDNA surveillance)

---

## Resource Budget

| Resource | Estimate |
|----------|----------|
| Download | ~20 GB (using pre-called data) |
| Disk total | ~100 GB |
| RAM peak | 32 GB (Scanpy) |
| CPU | 16 cores |
| GPU | 4-12 hours Modal A100 (~$5-15) |
| Wall clock | ~24-48 hours end-to-end |

## Final Deliverables

| File | Description |
|------|-------------|
| `results/FINAL_neoantigen_candidates_ranked.csv` | Primary: ranked vaccine candidates with sequence + structural scores |
| `results/alphafold/outputs/pair_*/ranked_0.pdb` | 3D peptide-MHC complex structures |
| `results/scrna/target_discovery.pdf` | scRNA-seq UMAP showing FAP/B7H3/EphA2 expression |
| `results/TREATMENT_RECOMMENDATION.md` | Complete parallel treatment plan |
| `results/MONITORING_PROTOCOL.md` | ctDNA + imaging + scRNA-seq cadence |
