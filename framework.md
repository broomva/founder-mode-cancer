# The Three-Pillar Framework

Sid's approach mirrors startup methodology applied to healthcare. Instead of "manager mode" medicine (physician decides, patient complies), he operated in "founder mode" — taking ownership of strategy while delegating execution to specialists.

## Pillar 1: Maximal Diagnostics

> Test everything, frequently, and own your data.

### Principle
Don't wait for symptoms to guide next steps. Run every diagnostic modality available to build a complete molecular picture of the cancer, then use that picture to drive treatment decisions.

### What This Looked Like

**Genomics (DNA)**
- Gene panels: UC500, Tempus xT
- Whole exome sequencing (WES): 5 providers (Personalis, Altera, Tempus, CeGaT, BostonGene)
- Whole genome sequencing (WGS): Personalis, UCLA (multiple timepoints)
- Copy number variation (CNV): ASCAT analysis from WGS

**Transcriptomics (RNA)**
- Bulk RNA-seq: 5 providers across multiple timepoints
- Single-cell RNA-seq (scRNA-seq): 8 PBMC timepoints + 3 tumor biopsies (T1, T2, T3)
- Gene Set Enrichment Analysis (GSEA): Limma and DESeq2

**Liquid Biopsy (ctDNA)**
- Signatera (Natera): Circulating tumor DNA tracking
- Northstar: Tumor methylation signal
- Personalis: Parts per million tracking

**Functional Testing**
- Organoid drug testing (UCLA): Grow tumor cells, test drugs on them
- Mass response drug testing (Travera): Physical drug sensitivity

**Imaging**
- CT scans: Chest, abdomen-pelvis, CAP, T-spine, angiography
- MRI: T-spine, spine, brain, cardiac
- PET: 18F-FDG (metabolic), 18F-Na (bone), 68Ga-FAP (fibroblast), 68Ga-B7H3, 68Ga-EphA2
- H&E and IHC tissue imaging

**Flow Cytometry**
- B cell subsets, T cell subsets, MAIT cells — tracked over 18+ months

### Key Insight
Multi-modal diagnostics at research-grade frequency revealed what standard clinical tests missed: the cancer cells were overexpressing fibroblast markers (FAP), opening the door to FAP-targeted radioligand therapy.

---

## Pillar 2: Therapeutic Development

> Don't wait for clinical trials. Create personalized treatments.

### Principle
Use diagnostic findings to design treatments specific to this patient's cancer biology. Access experimental drugs through FDA expanded access (Individual Patient IND, Form 3926).

### What This Looked Like

**Personalized Vaccines**
- JLF v1, v2, v3: Peptide neoantigen vaccines based on tumor mutations
- CeGaT: Separate neoantigen vaccine from German provider
- mRNA neoantigen vaccine: Latest generation (2025-2026)
- Monitored via ELISPOT immune response assays and vaccine neoantigen overlap analysis

**Targeted Radioligand Therapy**
- 177Lu-FAPi: Lutetium-177 conjugated to FAP-targeting ligand
- 225Ac-FAPi: Actinium-225 alpha emitter version (more potent)
- Theranostic approach: diagnostic imaging (68Ga-FAP PET) confirms target, then therapeutic payload delivered

**Gene Therapy**
- DeltaRex-G: Retroviral gene therapy (May-Aug 2024)

**Oncolytic Viruses**
- AdaPT-001: Intratumoral and subcutaneous injections (Oct 2024 - Aug 2025)

**Cell Therapies**
- SNK-01: NK cell therapy with multiple booster doses (Aug 2024 - Mar 2025)
- Autologous adipose-derived mesenchymal stem cells + exosomes (Feb 2026)

### Regulatory Mechanism
- FDA Form 3926 (Individual Patient Expanded Access IND)
- All applications approved within 48 hours
- The FDA proved more accommodating than hospital IRBs

---

## Pillar 3: Parallel Treatment

> Don't wait for one thing to fail. Test multiple hypotheses simultaneously.

### Principle
Standard oncology operates sequentially: try Treatment A, wait, scan, if failed try Treatment B. This is slow and loses ground to the cancer. Instead, layer compatible treatments and use diagnostics to measure what's working.

### What This Looked Like

During peak treatment (late 2024), Sid was simultaneously receiving:
- Checkpoint inhibitors (Dostarlimab + Ipilimumab)
- Neoantigen vaccines (JLF + CeGaT peptide vaccines)
- Oncolytic virus (AdaPT-001)
- NK cell therapy (SNK-01)
- Radioligand therapy (177Lu-FAPi / 225Ac-FAPi)
- XGeva (bone-targeted monoclonal antibody)

Each modality attacks the cancer from a different angle:
- Checkpoint inhibitors: remove the brakes on immune cells
- Vaccines: train the immune system to recognize tumor neoantigens
- Oncolytic virus: directly infect and kill cancer cells, release antigens
- NK cells: innate immune killing
- Radioligand: targeted radiation to FAP+ cells
- XGeva: inhibit osteoclast-mediated bone destruction

### Measuring What Works
- ctDNA (Signatera, Northstar, Personalis): Track circulating tumor DNA levels
- scRNA-seq of PBMCs: Monitor immune cell composition changes over time
- Imaging: PET/CT/MRI at regular intervals
- Flow cytometry: Track B cell and T cell subset dynamics

### Result
Immune infiltration shifted from 19% T cells to 89% T cells in the tumor. The combined assault turned a "cold" tumor "hot" — making it visible and vulnerable to the immune system.
