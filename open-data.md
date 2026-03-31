# Open Data Initiative

## Overview

Sid made the extraordinary decision to open-source all of his cancer data — 25 terabytes of genomic, transcriptomic, imaging, and clinical data — publicly available on Google Cloud.

This is one of the most comprehensive single-patient cancer datasets ever made publicly available.

---

## Data Portal: osteosarc.com

The interactive data portal provides visualization and exploration tools for all data types.

### Available Sections

| Section | Description |
|---------|-------------|
| **Timeline** | Interactive treatment timeline (Nov 2022 - Mar 2026) |
| **RNA-seq** | Bulk RNA-seq gene expression explorer (BostonGene, Tempus, Personalis) with GTEx/PCAWG comparisons |
| **scRNA-seq** | Single-cell data: 3 tumor biopsies (T1-T3), 8 PBMC timepoints |
| **GSEA** | Gene Set Enrichment Analysis (Limma + DESeq2) across tumor scRNA-seq clusters |
| **Imaging** | 12 tissue specimen images (H&E, IHC) |
| **Vaccines** | UpSet plots of neoantigen overlap across 5 vaccines + VAF trends + ELISPOT |
| **CNV** | ASCAT copy number analysis from WGS (T1 Jun 2024, T2 Jan 2025) |
| **BAMs** | IGV genome browser for WGS, long-read, scRNA-seq, RNA-seq |
| **Cell Lines** | HOS, U-2 OS, CAL-72 reference osteosarcoma lines with genomic profiles |
| **Data Files** | Direct access to 25TB dataset on Google Cloud |

---

## Dataset Contents

### Genomics
- Bulk whole genome sequencing (WGS)
- Whole exome sequencing (WES)
- HLA typing

### Transcriptomics
- Bulk RNA-seq (multiple providers, multiple timepoints)
- Single-cell RNA-seq (10x Genomics)
- Spatial transcriptomics

### Long-Read Sequencing
- Oxford Nanopore Technologies (ONT)

### Imaging
- H&E stained sections
- Immunohistochemistry (IHC)

### Storage
- **Size**: 25 TB
- **Platform**: Google Cloud Storage
- **Access**: Publicly readable buckets
- **Documentation**: Google Doc with bucket URLs and file descriptions

---

## Why Open-Source the Data

### For Research
- Osteosarcoma is rare — every data point matters
- Multi-modal longitudinal data from a single patient is exceptionally valuable
- Enables researchers worldwide to study treatment response dynamics
- scRNA-seq data shows immune microenvironment evolution pre/post-treatment

### For Future Patients
- Other osteosarcoma patients can compare their molecular profiles
- Treatment response data informs clinical decisions
- Vaccine neoantigen data helps validate prediction pipelines

### For Science
- Benchmark dataset for computational biology methods
- Ground truth for liquid biopsy sensitivity comparisons
- Reference for immune infiltration quantification
- Test case for AI-driven treatment recommendation systems

---

## Contact

cancer@sytse.com

---

## Significance

Most cancer patients never see their own genomic data. Sid not only obtained it all but made it available to the world. This is a radical act of transparency that:

1. Challenges the proprietary model of clinical sequencing companies
2. Demonstrates what comprehensive cancer profiling looks like
3. Creates a public resource for the osteosarcoma research community
4. Sets a precedent for patient-driven open science
