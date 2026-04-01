# Public Cancer Datasets for Founder-Mode-Oncology Pipeline Testing

> Compiled 2026-03-31. All sources listed are open access or have clear free-access paths.

---

## 1. Osteosarcoma-Specific Data

### 1.1 Sid Sijbrandij's Osteosarcoma Data (osteosarc.com)

The single most comprehensive open osteosarcoma dataset in existence. Sid Sijbrandij (GitLab co-founder) has published **~25 TB** of multi-omic data from his own tumor biopsies.

| Field | Details |
|-------|---------|
| **URL** | https://osteosarc.com/ (portal), https://osteosarc.com/data/ (full data catalog) |
| **GCS Bucket** | `gs://osteosarc-genomics` |
| **GCS Console** | https://console.cloud.google.com/storage/browser/osteosarc-genomics |
| **Total Size** | 24.88 TiB |
| **Access** | Publicly readable GCS bucket -- `gsutil ls gs://osteosarc-genomics/` works without auth |
| **Contact** | cancer@sytse.com |

**Data Types (with bucket paths and sizes):**

| Data Type | Timepoints | Format | Example Path | Size |
|-----------|------------|--------|-------------|------|
| **WGS** (130x coverage) | T0, T1, T2 | FASTQ + BAM | `genomics/genomics-bulk/2025.01.06/DNA/2025.01.06.dna.WGS/fastqs/tumor` | ~2 TB per timepoint |
| **WES** | T0, T1 | FASTQ | `genomics/genomics-bulk/2024.06.06/DNA/2024.06.06.dna.bostongene.WES/` | ~20 GB |
| **Bulk RNA-seq** | T0, T1, T2 (BostonGene, Tempus, Personalis, UCLA) | FASTQ + STAR BAM | `rna-seq/fastq/` | ~100 GB total |
| **scRNA-seq (tumor)** | T1, T2, T3 (10x GEX + TCR + BCR + CITE) | FASTQ + BAM + Seurat RDS | `ucsf/T1/FASTQ/` | ~300 GB FASTQ, ~5 GB Seurat objects |
| **scRNA-seq (PBMC)** | 8 longitudinal timepoints (Jan-Dec 2025) | FASTQ + Cell Ranger + Seurat | `hudson_lab/PBMC_scRNAseq/` | ~5.5 TiB |
| **ONT long-read scRNA** | T1, T2, T3 | FASTQ + BAM | `ONT/IPISRC044_ONT_upload/` | ~1 TiB |
| **PacBio long-read** | T1 | BAM | `ucsf/T1/pacbio_bams/` | 287 GB |
| **Spatial transcriptomics** | Visium HD + Phenocycler Fusion | h5mu, web summaries | `elucidate/` | ~413 GB |
| **Xenium** | T0 (2 blocks) | Xenium output | `xenium/T0/` | ~67 GB |
| **Multiplex imaging (ORION)** | T0 | OME-TIFF + Minerva | `hms_spatial/` | ~974 GB |
| **H&E + IHC pathology** | Multiple | CZI, TIFF | `pathology_images/`, `elucidate/HE_images/` | ~160 GB |
| **HLA typing** | Full Class I + II | Red Cross results | Listed on data page | Metadata |
| **Variant calls** | T1, T2 | VCF (Sarek 3.5.1: Mutect2, Strelka, FreeBayes, etc.) | `genomics_reprocessing/DNA/T2_2025_01_WGS_sarek_variants/` | ~2 GB |
| **CNV** | T1, T2 | ASCAT, CNVkit | `genomics_reprocessing/` | ~1 GB |
| **Neoantigen predictions** | Multiple | Spreadsheet + files | `neoantigen_prediction/` (178 MB) | 178 MB |

**Bonus resources on osteosarc.com:**
- Interactive scRNA-seq explorer: https://osteosarc.com/app/
- BAM browser (IGV.js): https://osteosarc.com/bams/
- GSEA explorer: https://osteosarc.com/gsea/
- CNV browser: https://osteosarc.com/cnv/
- Vaccine neoantigen overlap tracker: https://osteosarc.com/vaccines/
- Treatment timeline: https://osteosarc.com/timeline/
- Neoantigen vaccine overlap spreadsheet: https://docs.google.com/spreadsheets/d/17RE_Yyst9LzeNW_F6XcbV_RW3nYNgTuxopSWbGL0ozA/
- Colab notebooks for programmatic access: https://colab.research.google.com/drive/1fEFvCdUfQNn4jnSJRLCZUQDrXEf_Ujs7

**Pattern Unify (RCRF) API access:**
- Request access: email unify-admin@rcrf.org
- Portal: https://data-commons.rcrf-dev.org
- Python library: https://github.com/rcrf/patternq

### 1.2 GEO Osteosarcoma scRNA-seq Datasets

| Accession | Description | Cells | Samples | Platform | Access |
|-----------|-------------|-------|---------|----------|--------|
| **GSE152048** | scRNA-seq of 11 osteosarcoma lesions (primary, recurrent, metastatic) | 100,987 cells | 11 samples | 10x Genomics | Direct download from GEO/SRA |
| **GSE162454** | scRNA-seq of treatment-naive primary osteosarcoma | 29,278 cells | 6 patients | 10x Genomics | Direct download from GEO/SRA |

- **URL**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152048
- **URL**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162454
- **Combined**: 27 osteosarcoma samples, ~110,000 cells after QC
- **Download**: `wget` from GEO supplementary files or `prefetch`/`fasterq-dump` from SRA
- **Size estimate**: ~5-20 GB per dataset (processed matrices ~500 MB each)

### 1.3 GEO Osteosarcoma Bulk RNA-seq Datasets

| Accession | Description | Samples | Access |
|-----------|-------------|---------|--------|
| **GSE42352** | Osteosarcoma expression profiles | 103 samples | GEO direct download |
| **GSE39055** | Osteosarcoma gene expression | 37 samples | GEO direct download |
| **GSE33383** | Osteosarcoma with clinical outcomes | 84 samples | GEO direct download |
| **GSE21257** | Osteosarcoma metastasis expression | 53 samples | GEO direct download |
| **GSE117570** | Osteosarcoma bulk RNA-seq | Variable | GEO direct download |

### 1.4 TARGET Osteosarcoma (TARGET-OS)

| Field | Details |
|-------|---------|
| **URL** | https://portal.gdc.cancer.gov/ (filter: Program = TARGET, Project = TARGET-OS) |
| **Catalog** | https://datacatalog.ccdi.cancer.gov/dataset/TARGET-OS |
| **Samples** | 88+ patients |
| **Data types** | Gene expression array, copy number array, methylation, WGS, WES, miRNA-seq, mRNA-seq |
| **Open access** | Gene expression quantification, somatic MAFs (masked/filtered). **Note**: Raw BAMs and unmasked MAFs require dbGaP due to pediatric privacy. |
| **Download** | GDC Data Transfer Tool (`gdc-client`) or GDC API |
| **R package** | `TCGAbiolinks` for programmatic access |

### 1.5 Osteosarcoma Explorer (OSE)

| Field | Details |
|-------|---------|
| **URL** | https://datacommons.swmed.edu/cce/ose/ |
| **Patients** | 573 (largest osteosarcoma research data commons) |
| **Data types** | Clinical, genomic, protein, tissue imaging |
| **Sources** | TARGET, institutional collections |
| **Access** | Web portal with search, download, online analysis |

### 1.6 Cancer Imaging Archive (TCIA) -- Osteosarcoma

| Field | Details |
|-------|---------|
| **URL** | https://www.cancerimagingarchive.net/collection/osteosarcoma-tumor-assessment/ |
| **Data types** | Whole-slide H&E images for viable/necrotic tumor assessment |
| **Access** | Public download via TCIA |

---

## 2. General Cancer Genomics (Pipeline Testing)

### 2.1 TCGA via GDC (The Cancer Genome Atlas)

The gold standard for pan-cancer genomics. **33 cancer types, 11,000+ patients, ~2.5 PB total**.

| Field | Details |
|-------|---------|
| **Portal** | https://portal.gdc.cancer.gov/ |
| **Download tool** | `gdc-client` -- https://gdc.cancer.gov/access-data/gdc-data-transfer-tool |
| **API** | https://api.gdc.cancer.gov/ |
| **GitHub** | https://github.com/NCI-GDC/gdc-client |

**Open-access data types (NO login/dbGaP required):**

| Data Type | Format | How to Get |
|-----------|--------|-----------|
| Gene expression quantification | TSV (STAR counts) | GDC portal -> Download Manifest -> `gdc-client download -m manifest.txt` |
| Somatic mutation MAFs (masked) | MAF | Same as above; filter Data Type = "Masked Somatic Mutation" |
| Copy number segment files | TSV | GDC portal filter |
| miRNA expression | TSV | GDC portal filter |
| Clinical/demographic data | JSON/TSV | GDC portal or API |
| Biospecimen data | JSON/TSV | GDC portal or API |
| Pathology slide images | SVS | GDC portal |

**Controlled-access (requires dbGaP, ~weeks to approve):**
- Raw BAM/CRAM files (WGS, WES, RNA-seq)
- Unmasked somatic mutation MAFs
- Germline variants

**Quick-start for testing:**
```bash
# Install gdc-client
pip install gdc-client
# OR download binary from https://gdc.cancer.gov/access-data/gdc-data-transfer-tool

# Download a manifest from portal.gdc.cancer.gov, then:
gdc-client download -m gdc_manifest.txt

# Or download individual files by UUID:
gdc-client download <uuid>
```

### 2.2 UCSC Xena (Pre-processed TCGA + More)

The easiest way to get TCGA data in analysis-ready formats.

| Field | Details |
|-------|---------|
| **URL** | https://xenabrowser.net/ |
| **TCGA Hub** | https://tcga.xenahubs.net/ |
| **PCAWG Hub** | https://pcawg.xenahubs.net/ |
| **Data types** | SNVs, indels, SVs, CNV, gene/transcript/exon expression, DNA methylation, clinical |
| **Format** | TSV (tab-separated), ready for analysis |
| **33 TCGA cohorts** + Pan-Cancer (PANCAN) cohort |
| **Access** | Direct download, no login. Also R package `UCSCXenaTools` |
| **Size** | Individual cohort files are MB to low-GB range |

```r
# R programmatic access
install.packages("UCSCXenaTools")
library(UCSCXenaTools)
xe <- XenaHub(hostName = "tcgaHub")
```

### 2.3 cBioPortal

| Field | Details |
|-------|---------|
| **URL** | https://www.cbioportal.org/ |
| **Datasets** | 400+ cancer studies, 13,000+ tumor samples |
| **Data types** | Somatic mutations, CNAs, mRNA expression, miRNA, methylation, protein abundance, clinical |
| **Access** | No login for public datasets. Web UI + API + bulk download |
| **API** | https://www.cbioportal.org/api |
| **PCAWG study** | https://www.cbioportal.org/study?id=pancan_pcawg_2020 |
| **Download** | Tab-delimited files per study, or use the `cbioportalR` R package |
| **Size** | Individual study downloads are MB to low-GB |

### 2.4 ICGC ARGO

| Field | Details |
|-------|---------|
| **URL** | https://platform.icgc-argo.org/ |
| **Docs** | https://docs.icgc-argo.org/ |
| **Goal** | 100,000 donors with uniform analysis |
| **Latest release** | Data Release 14.0 (March 2026) -- 1,528 new donors |
| **Access** | Clinical data: open. Molecular data: requires DACO approval (free, takes ~2-4 weeks) |
| **Legacy ICGC data** | Still available at https://dcc.icgc.org/ (portal retired June 2024, data still downloadable) |

### 2.5 PCAWG (Pan-Cancer Analysis of Whole Genomes)

| Field | Details |
|-------|---------|
| **Description** | 2,658 whole-cancer genomes + matched normals across 38 tumor types |
| **Portal** | https://dcc.icgc.org/pcawg |
| **Xena Hub** | https://pcawg.xenahubs.net/ (processed data, direct download) |
| **cBioPortal** | https://www.cbioportal.org/study?id=pancan_pcawg_2020 |
| **Data types** | Somatic SNVs, indels, SVs, CNAs, driver mutations, mutational signatures |
| **Open access** | Consensus variant calls, driver calls, mutational signatures available through Xena/cBioPortal |
| **Controlled** | Raw BAMs via ICGC DACO |

### 2.6 DepMap / CCLE (Cancer Cell Line Encyclopedia)

| Field | Details |
|-------|---------|
| **URL** | https://depmap.org/portal/ |
| **CCLE page** | https://depmap.org/portal/ccle/ |
| **Cell lines** | 1,771+ cancer cell lines |
| **Data types** | Mutations (18,784 genes), RNA expression (TPM), copy number, drug sensitivity, CRISPR dependency scores |
| **Format** | CSV/TSV, directly downloadable |
| **Access** | No login required for most data. Raw BAMs on AWS (open access). |
| **AWS** | https://registry.opendata.aws/depmap-omics-ccle/ |
| **Size** | Processed matrices: ~100 MB-1 GB. Raw BAMs: multi-TB on AWS |

---

## 3. Neoantigen / Vaccine-Relevant Data

### 3.1 Datasets with Matched Tumor/Normal WES + RNA-seq + HLA

These are the datasets most directly useful for testing the pVACtools neoantigen prediction pipeline.

| Dataset | Cancer Type | Data Types | Access | Accession |
|---------|-------------|------------|--------|-----------|
| **osteosarc.com** | Osteosarcoma | WGS + WES + RNA-seq + scRNA + HLA typing | Open GCS bucket | `gs://osteosarc-genomics` |
| **Ott et al. 2017** (Nature) | Melanoma | WES (tumor+normal) + RNA-seq | dbGaP (controlled) | phs001451.v1.p1 |
| **Keskin et al. 2019** (Nature) | Glioblastoma | WES (tumor+normal) + RNA-seq | dbGaP | Study referenced in Nature 2019 |
| **TCGA (any cohort)** | 33 cancer types | WES + RNA-seq (open: expression + masked MAFs) | Open + dbGaP | portal.gdc.cancer.gov |
| **Multi-adjuvant vaccine 2025** (Cell) | Melanoma | WES + RNA-seq + scRNA + scTCR | dbGaP | phs003919 |

**For testing pVACtools without dbGaP access:**
- Use **osteosarc.com** data (fully open: WES VCFs + RNA-seq + HLA typing all available)
- Use TCGA **open-access masked somatic MAFs** + **gene expression quantification** (sufficient for basic pVACseq testing with synthetic HLA types)
- Use CCLE cell line data (mutations + expression, no matched normal but useful for pipeline smoke tests)

### 3.2 IEDB (Immune Epitope Database)

| Field | Details |
|-------|---------|
| **URL** | https://www.iedb.org/ |
| **Scope** | Infectious disease, allergy, autoimmune epitopes (NOT cancer -- see CEDAR below) |
| **Size** | 95%+ of published epitope data |
| **Access** | Free search, API, bulk export |
| **API** | https://www.iedb.org/api/ |
| **Tools** | MHC binding prediction, T cell epitope prediction, B cell epitope prediction |
| **Download** | Customizable data exports via web or API |

### 3.3 CEDAR (Cancer Epitope Database and Analysis Resource)

| Field | Details |
|-------|---------|
| **URL** | https://cedar.iedb.org/ |
| **Scope** | Cancer-specific epitopes (companion to IEDB, funded by NCI) |
| **Size** | 224,355+ epitopes from 6,240+ publications |
| **Assays** | 34,889 T cell assays, 3,780 B cell assays, 278,068 MHC ligand elution assays |
| **Receptors** | 3,526 TCRs, 108 antibodies |
| **Categories** | Neoantigens, viral antigens, germline/self antigens |
| **Access** | Free search and download at cedar.iedb.org |
| **Use case** | Validate predicted neoantigens against known immunogenic epitopes |

### 3.4 TumorAgDB (Tumor Neoantigen Database)

| Field | Details |
|-------|---------|
| **URL** | https://academic.oup.com/database/article/doi/10.1093/database/baaf010/8020156 |
| **Scope** | Curated tumor neoantigen data |
| **Access** | Open access database |

---

## 4. Protein Structures for AlphaFold Workflow Testing

### 4.1 Experimental Crystal Structures (RCSB PDB)

All freely downloadable from https://www.rcsb.org/ in PDB/mmCIF format.

| Target | UniProt | PDB ID(s) | Description | Resolution |
|--------|---------|-----------|-------------|-----------|
| **FAP** (Fibroblast Activation Protein) | Q12884 | **1Z68** | Crystal structure of human FAP alpha | 2.0 A |
| | | **9DVR** | Cryo-EM of human FAP alpha dimer + SUMO-I3 VHHs | Recent (2025) |
| **B7-H3** (CD276) | Q5ZPR3 | **4I0K** | Crystal structure of murine B7-H3 extracellular domain | - |
| | | **5CMA** | Anti-B7-H3 mAb ch8H9 Fab fragment | 2.5 A |
| **EphA2** | P29317 | **6B9L** | EphA2 with peptide 135E2 | - |
| | | **6NJZ** | EphA2 LBD + YSA peptide | - |
| | | **5NKA** | EphA2 kinase + compound 2g | - |
| **PD-1/PD-L1 complex** | Q15116/Q9NZQ7 | **3BIK** | Crystal structure of PD-1/PD-L1 complex | - |
| **PD-L1 alone** | Q9NZQ7 | **4Z18** | Crystal structure of human PD-L1 | - |
| **PD-L1 + inhibitor** | | **5O45**, **7OUN**, **8ALX** | PD-L1 with small-molecule/macrocyclic inhibitors | - |
| **PD-1 + high-affinity mutant** | | **5IUS** | PD-L1 + high-affinity PD-1 mutant | - |

**Download any structure:**
```bash
# PDB format
wget https://files.rcsb.org/download/1Z68.pdb

# mmCIF format
wget https://files.rcsb.org/download/1Z68.cif
```

### 4.2 Peptide-MHC Crystal Structures (for neoantigen validation)

| PDB ID | Description | Use Case |
|--------|-------------|----------|
| **3MRG** | HLA-A2 + HCV NS3 nonapeptide | Template for peptide-MHC docking |
| **2X4T** | HLA-A2.1 + cleavable peptide | Peptide-MHC binding validation |
| **5VGE**, **3RL1**, **3RL2** | Various HLA + peptide complexes | Docking templates for different HLA alleles/peptide lengths |

HLA-A*02:01 is the most studied allotype with >90% of deposited pMHC structures. Useful benchmarks:
- Melanoma neoantigen AVGSYVYSV bound to HLA-A*02:01 (1.9 A resolution)
- Phosphopeptide neoantigens bound to HLA-B*07:02

**Search for more:** https://www.rcsb.org/search?q=HLA%20peptide

### 4.3 AlphaFold Protein Structure Database

| Field | Details |
|-------|---------|
| **URL** | https://alphafold.ebi.ac.uk/ |
| **Download** | https://alphafold.ebi.ac.uk/download |
| **Coverage** | 214+ million predicted structures |
| **Format** | PDB + mmCIF |
| **Access** | Free, no login. Search by UniProt accession or protein name |
| **Human proteome** | Bulk download available (~23 GB compressed) |

**Get specific cancer target predictions:**
```bash
# FAP (Q12884)
wget https://alphafold.ebi.ac.uk/files/AF-Q12884-F1-model_v4.pdb

# B7-H3/CD276 (Q5ZPR3)
wget https://alphafold.ebi.ac.uk/files/AF-Q5ZPR3-F1-model_v4.pdb

# EphA2 (P29317)
wget https://alphafold.ebi.ac.uk/files/AF-P29317-F1-model_v4.pdb

# PD-1 (Q15116)
wget https://alphafold.ebi.ac.uk/files/AF-Q15116-F1-model_v4.pdb

# PD-L1 (Q9NZQ7)
wget https://alphafold.ebi.ac.uk/files/AF-Q9NZQ7-F1-model_v4.pdb
```

---

## 5. Liquid Biopsy / ctDNA

### 5.1 SEQC2 Oncopanel Liquid Biopsy Benchmark

The most comprehensive public ctDNA benchmarking dataset.

| Field | Details |
|-------|---------|
| **Publication** | [Nature Scientific Data 2022](https://www.nature.com/articles/s41597-022-01276-8) |
| **SRA Accession** | **SRP295025** (also referenced as SRP29602510 in some indices) |
| **Records** | 359 SRA records |
| **Total Size** | ~4.11 TB |
| **Formats** | FASTQ + BAM |
| **Platforms tested** | 5 industry ctDNA assays (Burning Rock, IDT, Illumina, Roche, Thermo Fisher) |
| **Sites** | 12 clinical/research facilities |
| **Variables** | Mutation frequencies, coverage depth, DNA input quantity |
| **Access** | Public via NCBI SRA: `prefetch SRP295025` |

### 5.2 BloodPAC Data Commons

| Field | Details |
|-------|---------|
| **URL** | https://data.bloodpac.org/ |
| **Platform** | Gen3 data commons (https://gen3.org) |
| **Data types** | ctDNA, CTC, protein, exosome assays + clinical data |
| **Access** | Account registration required (free), approved researchers get raw data |
| **API** | Gen3 API for programmatic queries and download |
| **Use case** | Liquid biopsy assay validation and cross-project analyses |

### 5.3 Pediatric Cancer cfDNA (Nature Communications 2021)

| Field | Details |
|-------|---------|
| **Publication** | [Nature Communications 2021](https://www.nature.com/articles/s41467-021-23445-w) |
| **Description** | Multimodal cfDNA whole-genome sequencing for pediatric cancers with low mutational burden |
| **Relevance** | Osteosarcoma is a pediatric cancer with low TMB -- directly relevant |
| **Access** | Check paper supplementary for data accession |

---

## 6. Quick-Start Recommendations

### For immediate pipeline testing (zero approval wait):

1. **Neoantigen calling (pVACtools)**: Use **osteosarc.com** -- has WES VCFs (Mutect2/Strelka from Sarek), RNA-seq BAMs, and full HLA typing. Download VCFs from `gs://osteosarc-genomics/genomics_reprocessing/DNA/T2_2025_01_WGS_sarek_variants/` and RNA from `gs://osteosarc-genomics/rna-seq/`.

2. **scRNA-seq analysis**: Download **GSE152048** (11 osteosarcoma samples, 100K cells) from GEO. Processed count matrices are small (~500 MB).

3. **Bulk expression + mutations**: Use **UCSC Xena** TCGA hub for instant TSV downloads of any of the 33 cancer types. No login needed.

4. **Protein structure validation**: Download PDB structures for FAP (1Z68), B7-H3 (4I0K), EphA2 (6B9L), PD-1/PD-L1 (3BIK) directly from RCSB. Compare against AlphaFold predictions.

5. **Cell line testing**: **DepMap/CCLE** has mutations + expression for 1,771 cell lines, downloadable as CSV with no login.

6. **ctDNA benchmarking**: **SEQC2** dataset on SRA (SRP295025), 4 TB of multi-platform liquid biopsy data.

### For comprehensive testing (1-4 weeks approval):

7. **TCGA controlled access**: Apply via dbGaP for raw WES/RNA-seq BAMs. Needed for running full variant calling from scratch.

8. **ICGC ARGO**: Apply for DACO approval for the latest pan-cancer molecular data (100K+ donors planned).

---

## 7. Access Method Summary

| Method | Tool | Install |
|--------|------|---------|
| GCS bucket (osteosarc) | `gsutil` | `pip install gsutil` or `gcloud` CLI |
| GDC/TCGA | `gdc-client` | https://gdc.cancer.gov/access-data/gdc-data-transfer-tool |
| GEO/SRA | `prefetch` + `fasterq-dump` | SRA Toolkit: https://github.com/ncbi/sra-tools |
| cBioPortal | Web or `cbioportalR` | https://www.cbioportal.org/api |
| UCSC Xena | Web or `UCSCXenaTools` (R) | `install.packages("UCSCXenaTools")` |
| PDB structures | `wget` | Direct HTTP |
| AlphaFold | `wget` | Direct HTTP |
| DepMap/CCLE | Web download | https://depmap.org/portal/data_page/ |
| BloodPAC | Gen3 API | https://data.bloodpac.org/ |
| IEDB/CEDAR | Web + API | https://cedar.iedb.org/ |

---

## Sources

- [osteosarc.com](https://osteosarc.com/) -- Sid Sijbrandij's Osteosarcoma Data
- [osteosarc.com/data](https://osteosarc.com/data/) -- Full data catalog with GCS paths
- [GDC Data Portal](https://portal.gdc.cancer.gov/) -- TCGA/TARGET data
- [UCSC Xena](https://xenabrowser.net/) -- Pre-processed TCGA and pan-cancer data
- [cBioPortal](https://www.cbioportal.org/) -- Cancer genomics visualization and download
- [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/) -- Gene Expression Omnibus
- [ICGC ARGO](https://platform.icgc-argo.org/) -- International Cancer Genome Consortium
- [DepMap Portal](https://depmap.org/portal/) -- Cancer Dependency Map / CCLE
- [RCSB PDB](https://www.rcsb.org/) -- Protein Data Bank
- [AlphaFold DB](https://alphafold.ebi.ac.uk/) -- Predicted protein structures
- [IEDB](https://www.iedb.org/) -- Immune Epitope Database
- [CEDAR](https://cedar.iedb.org/) -- Cancer Epitope Database and Analysis Resource
- [BloodPAC](https://data.bloodpac.org/) -- Liquid Biopsy Data Commons
- [Osteosarcoma Explorer](https://datacommons.swmed.edu/cce/ose/) -- OSE Data Commons
- [SEQC2 ctDNA study](https://www.nature.com/articles/s41597-022-01276-8) -- Liquid biopsy benchmark
- [Ott et al. 2017](https://pubmed.ncbi.nlm.nih.gov/28678778/) -- Melanoma neoantigen vaccine trial
- [Keskin et al. 2019](https://www.nature.com/articles/s41586-018-0792-9) -- Glioblastoma neoantigen vaccine trial
- [Going Founder Mode on Cancer](https://centuryofbio.com/p/sid) -- Elliot Hershberg profile of Sid's approach
- [Sijbrandij Substack](https://sijbrandij.substack.com/p/im-going-founder-mode-on-my-cancer) -- Original founder-mode post
- [TARGET OS](https://www.cancer.gov/ccg/research/genome-sequencing/target/studied-cancers/osteosarcoma) -- NCI TARGET Osteosarcoma
- [PCAWG](https://www.nature.com/articles/s41586-020-1969-6) -- Pan-Cancer Analysis of Whole Genomes
- [TCIA Osteosarcoma](https://www.cancerimagingarchive.net/collection/osteosarcoma-tumor-assessment/) -- Cancer Imaging Archive
