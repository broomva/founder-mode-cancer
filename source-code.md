# Source Code and Open-Source Toolchain

## osteosarc.com — Data Portal

The osteosarc.com data portal does not appear to have a public source code repository. It is likely a custom-built internal application. Key technical observations:

- Multiple specialized bioinformatics visualization tools integrated
- IGV genome browser embedded for BAM browsing
- Interactive timeline visualization
- UpSet plots for vaccine neoantigen overlap
- Google Cloud Storage backend (25TB in public buckets)
- No GitHub org found at `github.com/osteosarc`
- Sid's personal GitHub (`sytses`) has no cancer-related repos

---

## Open-Source Toolchain Used in the Approach

The bioinformatics pipeline Sid's team used can be reconstructed from publicly available tools:

### 1. Neoantigen Vaccine Design

**openvax/neoantigen-vaccine-pipeline** (Python, 90 stars)
- https://github.com/openvax/neoantigen-vaccine-pipeline
- Used in two Phase I clinical trials (NCT02721043, NCT03223103)
- Pipeline: alignment (BWA) → processing (GATK) → variant calling (Mutect/Strelka) → neoantigen ranking (Vaxrank)
- Inputs: Tumor/normal WES + tumor RNA-seq + HLA typing
- Outputs: Ranked vaccine peptide candidates

**philfung/openvaxx** (JavaScript, 67 stars)
- https://github.com/philfung/openvaxx
- Complete guide: biopsy → sequencing → mutation detection → AI target selection → mRNA synthesis → LNP formulation → QC
- Cost estimate: $4,200 in-house, $9,700-$13,400 outsourced per patient
- Timeline: ~4-6 weeks biopsy to final product
- Equipment capital: $500k-$800k for in-house production

### 2. Variant Calling & Genomics

**GATK (Genome Analysis Toolkit)**
- https://github.com/broadinstitute/gatk
- Mutect2 for somatic variant calling
- Industry standard for tumor/normal paired analysis

**Strelka2** (Illumina)
- https://github.com/Illumina/strelka
- Fast somatic variant caller

**BWA** (Burrows-Wheeler Aligner)
- https://github.com/lh3/bwa
- DNA alignment to reference genome

**STAR** (Spliced Transcripts Alignment to a Reference)
- https://github.com/alexdobin/STAR
- RNA-seq alignment

### 3. Neoantigen Prediction

**pVACtools** (personalized Variant Antigens by Cancer)
- https://github.com/griffithlab/pVACtools
- pVACseq: neoantigen prediction from somatic mutations
- pVACvector: optimal vaccine sequence design
- Integrates with multiple MHC binding predictors

**MHCflurry**
- https://github.com/openvax/mhcflurry
- Neural network MHC-I peptide binding prediction
- Used in Step 3 (AI-driven target selection) of the openvaxx pipeline

### 4. Single-Cell Analysis

**10x Genomics Cell Ranger**
- Proprietary but freely downloadable
- Processes 10x Chromium scRNA-seq data
- Produces gene expression matrices from raw FASTQ

**Scanpy** (Python) / **Seurat** (R)
- https://github.com/scverse/scanpy
- https://github.com/satijalab/seurat
- Standard tools for scRNA-seq analysis, clustering, differential expression

### 5. Copy Number Analysis

**ASCAT** (Allele-Specific Copy number Analysis of Tumours)
- https://github.com/VanLoo-lab/ascat
- Used for CNV analysis in Sid's WGS data (T1, T2 timepoints)

**ezASCAT** — Convenient R wrapper
- https://github.com/CompEpigen/ezASCAT

### 6. Gene Set Enrichment

**Limma** (R/Bioconductor)
- Linear models for microarray and RNA-seq data
- Used for GSEA in tumor scRNA-seq

**DESeq2** (R/Bioconductor)
- Differential expression analysis
- Used alongside Limma for GSEA

### 7. Genome Browser

**IGV** (Integrative Genomics Viewer)
- https://github.com/igvteam/igv
- Web-embedded version for BAM browsing on osteosarc.com
- Supports WGS, long-read, scRNA-seq, RNA-seq tracks

### 8. mRNA Vaccine Synthesis (Physical)

**LinearDesign** (Stanford)
- RNA sequence optimization for stable secondary structure
- Codon optimization for expression efficiency

Equipment stack (from openvaxx):
- Telesis Bio BioXp (~$100k): DNA synthesis
- NTxscribe System (~$250k): In vitro transcription
- NanoAssemblr (~$150k): LNP formulation
- Stunner DLS (~$80k): QC

### 9. Liquid Biopsy / ctDNA

Commercial platforms (not open-source):
- **Signatera** (Natera): Tumor-informed ctDNA
- **Northstar**: Methylation-based
- **Personalis**: Ultra-sensitive PPM

---

## Generalizable Open-Source Pipeline

A reproducible version of Sid's approach using only open-source tools:

```
Step 1: Sequencing
  └── WGS + WES + RNA-seq + scRNA-seq (10x)

Step 2: Alignment
  ├── BWA (DNA → reference genome)
  └── STAR (RNA → reference genome)

Step 3: Variant Calling
  ├── GATK Mutect2 (somatic SNVs/indels)
  └── Strelka2 (validation caller)

Step 4: Copy Number
  └── ASCAT (allele-specific CNV from WGS)

Step 5: Single-Cell Analysis
  ├── Cell Ranger (10x data processing)
  ├── Scanpy/Seurat (clustering, DE analysis)
  └── Identify non-obvious targets (FAP, B7H3, EphA2)

Step 6: Gene Set Enrichment
  ├── Limma
  └── DESeq2

Step 7: Neoantigen Prediction
  ├── pVACseq (neoantigen candidates)
  ├── MHCflurry (MHC binding prediction)
  └── Vaxrank (candidate ranking)

Step 8: Vaccine Design
  ├── pVACvector (peptide vaccine sequence)
  └── LinearDesign (mRNA optimization)

Step 9: Monitoring
  ├── ctDNA assays (commercial)
  ├── Flow cytometry (B/T cell subsets)
  └── Serial scRNA-seq (immune evolution)

Step 10: Visualization
  └── IGV (genome browser)
```

---

## Related Research Repos

| Repo | Stars | Description |
|------|-------|-------------|
| cortes-ciriano-lab/osteosarcoma_evolution | 4 | Osteosarcoma genome complexity and evolution |
| dyammons/canine_osteosarcoma_atlas | 3 | scRNA-seq atlas of canine osteosarcoma |
| MSKCC-Computational-Pathology/DMMN-osteosarcoma | 6 | MSKCC computational pathology for osteosarcoma |
| zhengxj1/A-Single-Cell-and-Spatially-Resolved-Atlas-of-Human-Osteosarcomas | 3 | Human osteosarcoma single-cell atlas |
