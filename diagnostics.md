# Diagnostic Strategy

## Philosophy

> Standard oncology runs a few tests and treats based on population statistics. Founder mode runs every test and treats based on this patient's specific biology.

Sid pursued research-grade diagnostics at clinical frequency — the kind of data density typically only seen in academic studies, not patient care.

---

## Genomic Profiling

### Gene Panels
| Date | Test | Provider |
|------|------|----------|
| 2022-11-14 | UC500 | UCSF |
| 2022-12-16 | Tempus xT | Tempus |

### Whole Exome Sequencing (WES)
| Date | Providers |
|------|-----------|
| 2022-12-16 | Personalis NextDx, Altera, Tempus xE, CeGaT, BostonGene |
| 2024-06-11 | BostonGene |

### Whole Genome Sequencing (WGS)
| Date | Provider |
|------|----------|
| 2022-12-16 | Personalis Next Personal Dx |
| 2024-06-06 | UCLA |
| 2025-01-28 | UCLA |

### Copy Number Variation (CNV)
ASCAT analysis from WGS at two timepoints:
- T1: June 2024
- T2: January 2025

---

## Transcriptomics

### Bulk RNA-seq
| Date | Providers |
|------|-----------|
| 2022-12-16 | BostonGene, Personalis NextDx, Altera, Tempus xR, CeGaT |
| 2024-06-06 | UCLA |
| 2024-06-11 | BostonGene |
| 2025-01-28 | UCLA |

Includes GTEx and PCAWG comparisons for context against normal tissue and pan-cancer datasets.

### Single-Cell RNA-seq (scRNA-seq)

**Tumor biopsies** (10x Genomics):
- T1, T2, T3 — three sequential timepoints showing immune landscape evolution

**CD3+ PBMCs** (peripheral blood):
| Date | Sample |
|------|--------|
| 2025-01-25 | PBMCs |
| 2025-04-09 | PBMCs |
| 2025-05-01 | PBMCs |
| 2025-06-25 | PBMCs |
| 2025-07-24 | PBMCs |
| 2025-08-21 | PBMCs |
| 2025-09-22 | PBMCs |
| 2025-11-06 | PBMCs |

### Gene Set Enrichment Analysis (GSEA)
- Methods: Limma and DESeq2
- Source: Tumor scRNA-seq (T1, T2, T3)
- Cluster levels: Two resolution levels

---

## Liquid Biopsy / ctDNA Monitoring

Three independent platforms tracked circulating tumor DNA:

### Signatera (Natera) — MTM/mL
Gold standard ctDNA assay. Most readings at 0 (undetectable). Key detections:
- 2024-06-11: **2.46** (recurrence confirmed)
- 2024-07-15: 0.08 (responding)
- 2024-08-19: 0.03 (near clearance)
- 2025-05-06: 0.01 (trace)

### Northstar — Tumor Methylation Signal (TMS)
Methylation-based liquid biopsy. Trend:
- Peak: 26 (Jul 2024, Sep 2024)
- Nadir: 10 (Nov 2025)
- Range: 10-26 over 18 months

### Personalis — PPM (logarithmic scale)
Ultra-sensitive detection:
- Peak: 963 PPM (Jun 2024, recurrence)
- Rapid decline: 21 PPM within 2 weeks
- Multiple "not detected" results through 2025-2026

---

## Functional Testing

### Organoid Drug Testing (UCLA, June 2024)
Grow tumor cells in 3D culture (organoids) and screen drugs against them ex vivo. Identifies which drugs actually kill this patient's specific cancer cells.

### Mass Response Drug Testing (Travera, June 2024)
Physical measurement of cell death in response to drugs. Complements genomic predictions with empirical drug sensitivity data.

---

## Imaging

### CT Scans (21 sessions)
- Chest, abdomen-pelvis, CAP (chest/abdomen/pelvis), T-spine, angiography
- Frequency: roughly monthly during active treatment

### MRI (26 sessions)
- T-spine (primary tumor site): most frequent
- Additional: full spine, brain, cardiac
- Used for soft tissue detail and surgical planning

### PET Scans (14 sessions)
Multiple tracers for different biological questions:

| Tracer | Target | Purpose |
|--------|--------|---------|
| 18F-FDG | Glucose metabolism | Standard tumor detection |
| 18F-Na | Bone turnover | Bone metastasis screening |
| 68Ga-FAP | Fibroblast activation protein | The breakthrough — confirmed FAP overexpression |
| 68Ga-B7H3 | B7-H3 immune checkpoint | Experimental target validation |
| 68Ga-EphA2 | Ephrin receptor A2 | Experimental target validation |

The 68Ga-FAP PET was the pivotal diagnostic: it confirmed the tumor expressed the FAP target, enabling radioligand therapy.

### Tissue Imaging
12 specimen images from osteosarcoma samples (H&E and IHC stains).

---

## Flow Cytometry

Tracked immune cell populations in peripheral blood over 18+ months (Jul 2024 - Jan 2026):

**T Cell Subsets (% of CD45)**
- B cells, T cells overall
- CD4 T cells (% of T cells)
- CD8 T cells (% of T cells)
- MAIT cells (% of T cells)

**B Cell Subsets (% of B cells)**
- IgD+CD27+ (memory)
- IgD+CD27- (naive)
- IgD- total, IgD-CD27+, IgD-CD27-
- Plasmablasts

---

## Pathology & Tissue

### Biopsies
| Date | Site | Institution |
|------|------|-------------|
| 2022-11-14 | T5 | UCSF |
| 2024-05-10 | T5 | UCSF |
| 2024-06-06 | T4 | UCLA |
| 2024-06-11 | T4/5 | UCLA |
| 2024-10-24 | Vaccination site | — |
| 2025-01-28 | T4/5 | UCLA |
| 2025-02-28 | Hilar lymph node | — |

### Surgeries
| Date | Site | Notes |
|------|------|-------|
| 2022-12-16 | T4/5 | Initial resection + titanium fusion |
| 2025-04-17 | T4/5 | Second resection (MSKCC) after tumor shrank |

---

## The Critical Insight

Standard clinical sequencing (gene panels, basic WES) would not have revealed the FAP overexpression. It took **single-cell RNA-seq** — a research-grade assay not typically used in clinical oncology — to reveal that the cancer cells were hijacking the fibroblast/wound-healing pathway.

This finding directly enabled:
1. 68Ga-FAP PET imaging → confirmed the target
2. 177Lu-FAPi radioligand therapy → delivered radiation to FAP+ cells
3. 225Ac-FAPi → more potent alpha-particle version
4. Tumor shrank enough for second surgery

Without maximal diagnostics, this treatment path would never have been discovered.
