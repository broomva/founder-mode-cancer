# Founder Mode on Cancer

Research compilation and agent skill for personalized cancer treatment, based on Sid Sijbrandij's (GitLab co-founder) approach to treating osteosarcoma using entrepreneurial principles, AI-assisted decision making, open-source bioinformatics, and structure-based protein design.

[![Skill](https://img.shields.io/badge/skill-founder--mode--oncology-blue)](https://github.com/broomva/founder-mode-oncology)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/broomva/founder-mode-oncology/blob/main/LICENSE)

## Background

In November 2022, Sid Sijbrandij was diagnosed with osteosarcoma — a rare bone cancer — in his T5 vertebra. After standard-of-care treatment and a 2024 recurrence, he applied "founder mode" thinking to his own healthcare: maximal diagnostics, parallel (not sequential) treatments, and personalized therapeutic development.

His cancer is now undetectable. Tumor-infiltrating T cells went from **19% to 89%**. His **25 TB** of genomic data is publicly available on Google Cloud.

## What This Repo Contains

### Research (14 files)

| File | Description |
|------|-------------|
| [overview.md](overview.md) | Case summary — diagnosis, standard care, founder mode pivot, outcome |
| [framework.md](framework.md) | Three-pillar decision framework (diagnostics, therapeutics, parallel treatment) |
| [timeline.md](timeline.md) | Complete chronological record (Nov 2022 - Mar 2026) — every scan, biopsy, drug |
| [diagnostics.md](diagnostics.md) | All diagnostic modalities: WGS, WES, scRNA-seq, ctDNA x3, organoids, PET tracers |
| [treatments.md](treatments.md) | Full catalog: chemo, checkpoint inhibitors, vaccines (5 versions), radioligand, gene therapy |
| [mrd-tracking.md](mrd-tracking.md) | Liquid biopsy data from 3 platforms with cross-platform comparison |
| [breakthroughs.md](breakthroughs.md) | 7 key turning points — scRNA-seq revealing FAP, immune shift 19%→89% |
| [systemic-barriers.md](systemic-barriers.md) | 7 systemic barriers: tissue access, IRBs, data portability, economics |
| [ai-role.md](ai-role.md) | How ChatGPT was used: literature review, decision support, balanced scorecards |
| [future-vision.md](future-vision.md) | Scaling vision: Even One Ventures, platform technologies, projected $175K cost |
| [open-data.md](open-data.md) | 25TB open dataset on Google Cloud, osteosarc.com portal |
| [secondary-conditions.md](secondary-conditions.md) | Complications: hip AVN, thyroid dysfunction, spinal infection |
| [resources.md](resources.md) | All links, people, institutions, technologies, statistics |
| [source-code.md](source-code.md) | Open-source toolchain: openvax, pVACtools, openvaxx, GATK, Scanpy |

### AlphaFold Integration

| File | Description |
|------|-------------|
| [alphafold-integration.md](alphafold-integration.md) | 4 structural biology workflows: neoantigen-MHC validation, radioligand modeling, de novo binder design, mutation impact analysis |

### Test Infrastructure

| File | Description |
|------|-------------|
| [public-datasets.md](public-datasets.md) | 461-line catalog of every open cancer genomics source (osteosarc.com GCS paths, TCGA, GEO, cBioPortal, IEDB/CEDAR, PDB, SEQC2) |
| [test-plan.md](test-plan.md) | 6-phase end-to-end pipeline test using Sid's actual data from `gs://osteosarc-genomics` |

### Packaged Skill

| File | Description |
|------|-------------|
| [founder-mode-oncology.skill](founder-mode-oncology.skill) | Packaged agent skill (zip) — installable across 37+ AI agents |

## Quick Install (Agent Skill)

```bash
npx skills add broomva/founder-mode-oncology
```

The skill packages the entire framework into 7 files (1,321 lines) with decision workflows, open-source pipeline references, regulatory navigation, MRD monitoring interpretation, and AlphaFold/RFdiffusion structural biology integration.

Skill repo: [github.com/broomva/founder-mode-oncology](https://github.com/broomva/founder-mode-oncology)

## Key Data Sources

| Source | URL | Access | Highlight |
|--------|-----|--------|-----------|
| osteosarc.com | [osteosarc.com](https://osteosarc.com) | Public GCS bucket | 24.88 TiB — WGS, WES, scRNA-seq, pre-called VCFs, HLA typing |
| GEO osteosarcoma | [GSE152048](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152048) | Direct download | 100K osteosarcoma single cells |
| TCGA | [portal.gdc.cancer.gov](https://portal.gdc.cancer.gov/) | Open MAFs, no login | 33 cancer types, 11K+ patients |
| CEDAR | [cedar.iedb.org](https://cedar.iedb.org/) | Free | 224K+ cancer epitopes |
| PDB (FAP) | [1Z68](https://www.rcsb.org/structure/1Z68) | Direct download | Crystal structure of FAP at 2.0 A |
| AlphaFold DB | [AF-Q12884-F1](https://alphafold.ebi.ac.uk/entry/Q12884) | Direct download | Predicted FAP structure |

See [public-datasets.md](public-datasets.md) for the complete catalog (30+ sources).

## Test Plan

The [test-plan.md](test-plan.md) defines a 6-phase pipeline test on Sid's actual data:

1. **Acquire** — Download pre-called VCFs + RNA-seq + scRNA-seq from `gs://osteosarc-genomics` (~20 GB)
2. **Annotate** — VEP annotation for pVACseq compatibility
3. **scRNA-seq** — Scanpy target discovery (confirm FAP, identify additional targets)
4. **Neoantigens** — pVACseq + MHCflurry + Vaxrank → top 50 candidates
5. **AlphaFold** — Multimer validation of peptide-MHC complexes (Modal A100)
6. **Treatment** — Full parallel combination recommendation using skill's decision workflow

**Budget**: ~24-48h wall clock, ~$5-15 cloud GPU. Zero approvals needed.

## Key Sources

- [sytse.com/cancer](https://sytse.com/cancer/) — Hub page
- [osteosarc.com](https://osteosarc.com) — Open data portal (25TB genomic/imaging data)
- [Century of Bio: Going Founder Mode on Cancer](https://centuryofbio.com/p/sid) — Elliot Hershberg's deep-dive article
- [Even One Ventures](https://evenone.ventures) — Venture fund scaling this approach
- [sijbrandij.substack.com](https://sijbrandij.substack.com) — Sid's newsletter
- OpenAI Forum: "Terminal to Turnaround: How GitLab's Co-Founder Leveraged ChatGPT in His Cancer Fight"

## Blog Post

Published on broomva.tech: [Founder Mode on Cancer: From Terminal Diagnosis to Open-Source Cure](https://broomva.tech/writing/founder-mode-cancer)

## Why This Matters

> "It costs $1B to get a drug approved. But it costs $1M to dose a single person with personalized therapy." — Sid Sijbrandij

The technologies for personalized cancer treatment exist today. The barriers are systemic: regulatory friction, hospital tissue-access policies, data portability, and business models optimized for blockbuster drugs over individualized medicine.

## License

MIT — see [founder-mode-oncology LICENSE](https://github.com/broomva/founder-mode-oncology/blob/main/LICENSE)
