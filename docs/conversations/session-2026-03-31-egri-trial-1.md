---
title: "EGRI Trial 1 — Founder Mode Oncology Pipeline"
date: 2026-03-31
end_date: 2026-04-01
branch: main
repos:
  - broomva/founder-mode-cancer
  - broomva/founder-mode-oncology
tags:
  - egri
  - oncology
  - osteosarcoma
  - neoantigen
  - scRNA-seq
  - alphafold
  - esmfold
  - open-source
  - skill-creator
  - pipeline
  - nuc-deployment
---

# EGRI Trial 1 — Founder Mode Oncology Pipeline

**Date:** 2026-03-31 to 2026-04-01
**Branch:** `main`
**Repos:** `broomva/founder-mode-cancer`, `broomva/founder-mode-oncology`

---

## Summary

End-to-end execution of the Founder Mode Cancer research pipeline — from literature review through neoantigen discovery and treatment recommendation. Delivered a published agent skill, a blog post, open-source documentation, and a 6-phase computational oncology pipeline run against real osteosarcoma genomic data.

---

## Key Events (Chronological)

### 1. Research Phase
Fetched and compiled sources from sytse.com/cancer, osteosarc.com, centuryofbio.com/p/sid, and evenone.ventures. Produced 14 research documents covering diagnostics, treatments, systemic barriers, open data, source code analysis, and future vision.

### 2. Source Code Analysis
Mapped the open-source oncology toolchain: [[openvax]], [[pVACtools]], [[openvaxx]], [[GATK]], [[Scanpy]]. Documented capabilities, gaps, and integration patterns in `source-code.md`.

### 3. Skill Creation
Created the `founder-mode-oncology` skill via `/skill-creator` — 7 files, 1,321 lines. Packages the full research pipeline as a reusable agent capability.

### 4. AlphaFold Integration
Added structural biology reference covering [[RFdiffusion]], [[ProteinMPNN]], and [[ESMFold]] workflows for peptide-MHC binding validation. Documented in `alphafold-integration.md`.

### 5. Skill Published
Published: `npx skills add broomva/founder-mode-oncology` — installed across 37 agents in the broomva workspace.

### 6. Blog Post #1
"Founder Mode on Cancer: From Terminal Diagnosis to Open-Source Cure" — PR #63 merged to broomva.tech.

### 7. OSS Documentation
Added README, LICENSE (MIT), and CONTRIBUTING.md to the skill repo. Full open-source onboarding package.

### 8. Data Catalog
Created `public-datasets.md` — 461 lines documenting 30+ public data sources with GCS bucket paths for `osteosarc-genomics`.

### 9. Test Plan
Designed a 6-phase pipeline: Acquire -> Annotate -> scRNA-seq -> Neoantigens -> Structure -> Treatment. Documented in `test-plan.md`.

### 10. NUC Deployment
Probed Intel NUC (32GB RAM, RTX 3060, Windows). Installed dependencies, fixed numpy compatibility. Established remote execution pattern.

### 11. Phase 1 — Acquire
Downloaded 1.29 GB from `gs://osteosarc-genomics` via HTTP (gsutil auth broken on NUC, bucket is public).

### 12. Phase 3 — scRNA-seq Analysis
- 4,452 cells processed, 17 clusters identified
- **FAP CONFIRMED** — log2FC=2.81, padj=2.07e-24
- 14 significant therapeutic targets discovered

### 13. Phase 4 — Neoantigen Prediction
- 12,420 epitopes screened
- **Top candidate:** VPS72 AREERALLP IC50=3.8nM
- **HLA alleles discovered:** A\*01:01, B\*08:01, B\*27:05, C\*01:02, C\*07:01

### 14. Phase 5 — ESMFold Structural Validation
- 2 Tier 1 candidates, 5 Tier 2 candidates after pLDDT rescaling
- Validated peptide folding confidence for top neoantigen binders

### 15. Phase 6 — Treatment Recommendation
5-layer combination recommendation generated integrating neoantigen vaccine candidates, checkpoint inhibitors, and targeted therapies.

---

## Key Discoveries

| Discovery | Detail |
|-----------|--------|
| VCFs pre-annotated | VCFs in the GCS bucket are pre-annotated with VEP — Phase 2 (annotation) is skippable |
| pVACtools baseline | pVACtools predictions already exist in bucket — serves as validation baseline |
| Sid's HLA typing | A\*01:01, B\*08:01, B\*27:05, C\*01:02, C\*07:01 |
| gsutil auth | Broken on NUC — HTTP downloads work because the bucket is public |
| numpy 2.4.4 breaks | pyarrow and scanpy break on numpy >= 2.4.4 — must pin `numpy<2` |
| ESMFold pLDDT scale | Returns pLDDT on 0-1 scale for short peptides — must rescale to 0-100 |

---

## Artifacts Produced

- `founder-mode-oncology.skill/` — 7 files, 1,321 lines
- `public-datasets.md` — 461 lines, 30+ sources
- `test-plan.md` — 6-phase pipeline design
- `results/` — Phase 3-6 output files
- Blog post: "Founder Mode on Cancer" (PR #63)
- README, LICENSE (MIT), CONTRIBUTING.md

---

## Related Sessions

- [[Conversations]] — Session index

---

*Bridged by knowledge-graph-memory skill on 2026-03-31.*
