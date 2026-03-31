# AlphaFold and Structural Biology Integration

## Why Structure Matters for Personalized Oncology

Sid's approach was primarily sequence-based (genomics, transcriptomics, neoantigen prediction). Adding structural biology unlocks several capabilities that could improve outcomes:

1. **Better neoantigen vaccine design** — predict 3D peptide-MHC binding, not just sequence-based affinity
2. **Radioligand optimization** — model ligand-target protein binding for FAP, B7H3, EphA2
3. **De novo therapeutic protein design** — design custom binders against tumor targets
4. **Drug repurposing** — screen existing drugs against predicted tumor protein structures
5. **Mutation impact analysis** — understand how tumor mutations alter protein structure and function

---

## Integration Points with the Three-Pillar Framework

### Pillar 1 (Maximal Diagnostics) + Structure

| Diagnostic Finding | Structure-Based Enhancement |
|--------------------|---------------------------|
| Somatic mutations (WES/WGS) | AlphaFold2 → predict mutant vs wildtype structure → identify structural consequences |
| scRNA-seq target discovery (FAP, B7H3) | AlphaFold DB → get target structure → identify druggable surfaces |
| Neoantigen candidates (pVACseq) | AlphaFold Multimer → predict peptide-MHC complex → validate binding geometry |
| Copy number amplifications | ESM embeddings → assess protein stability changes from amplified genes |

### Pillar 2 (Therapeutic Development) + Structure

| Treatment Type | Structure-Based Enhancement |
|----------------|---------------------------|
| Neoantigen vaccines | AlphaFold Multimer: model peptide-MHC-I complex → select candidates with strongest predicted binding geometry |
| Radioligand therapy | Molecular docking: model FAP-ligand binding → optimize FAPi targeting molecule |
| Custom binders | RFdiffusion → ProteinMPNN: de novo design of proteins that bind tumor-specific surfaces |
| CAR-T/CAR-NK | AlphaFold: predict scFv-antigen binding → optimize chimeric receptor design |
| Checkpoint inhibitors | Structural analysis: verify PD-1/PD-L1 binding not disrupted by tumor mutations |

### Pillar 3 (Parallel Treatment) + Structure

Structure prediction can prioritize which therapies to combine:
- Model each target protein → assess druggability → prioritize modalities with strongest structural rationale
- Predict interaction between combination drugs at the structural level

---

## Concrete Workflows

### Workflow 1: Structure-Guided Neoantigen Vaccine Design

Enhances the pVACseq → MHCflurry → Vaxrank pipeline with 3D validation.

```
Current pipeline (sequence-only):
  Mutations → pVACseq → MHCflurry (1D binding prediction) → Vaxrank → Vaccine

Enhanced pipeline (sequence + structure):
  Mutations → pVACseq → MHCflurry (1D binding) → TOP CANDIDATES
    → AlphaFold Multimer (peptide + MHC-I complex) → 3D binding validation
    → Filter: pLDDT >85, ipTM >0.5, PAE_interface <10
    → Re-rank by structural confidence → Vaccine
```

**Why this helps**: MHCflurry predicts binding from sequence alone. AlphaFold Multimer can predict the 3D structure of the peptide-MHC complex, revealing whether the peptide physically fits in the MHC groove. Candidates that score high on both sequence-based and structure-based metrics are more likely to generate strong immune responses.

**Implementation**:
```python
# For each top neoantigen candidate from pVACseq:
# 1. Get patient's HLA-I sequence (from OptiType)
# 2. Create FASTA with peptide + HLA chain
# 3. Run AlphaFold Multimer
# 4. Evaluate ipTM and interface PAE

# ColabFold command:
# modal run modal_colabfold.py \
#   --input-faa peptide_mhc_pairs.fasta \
#   --out-dir af_validation/ \
#   --model-type alphafold2_multimer_v3
```

### Workflow 2: Structure-Based Radioligand Target Validation

Goes beyond confirming FAP expression (PET imaging) to understanding the binding interface.

```
Target discovery (scRNA-seq) → FAP identified
  → AlphaFold DB: retrieve FAP structure (Q12884)
  → Identify surface-exposed epitopes
  → Molecular docking: model FAPi (FAPI-04, FAPI-46) binding pose
  → Assess binding pocket geometry → optimize ligand
  → Theranostic: same ligand for 68Ga (imaging) + 177Lu/225Ac (therapy)
```

**Key target structures from AlphaFold DB:**
| Target | UniProt | AlphaFold DB | Relevance |
|--------|---------|-------------|-----------|
| FAP | Q12884 | AF-Q12884-F1 | Primary radioligand target |
| B7-H3 (CD276) | Q5ZPR3 | AF-Q5ZPR3-F1 | Experimental PET/therapy target |
| EphA2 | P29317 | AF-P29317-F1 | Experimental PET/therapy target |
| PD-1 (PDCD1) | Q15116 | AF-Q15116-F1 | Checkpoint inhibitor target |
| PD-L1 (CD274) | Q9NZQ7 | AF-Q9NZQ7-F1 | Checkpoint inhibitor target |
| CTLA-4 | P16410 | AF-P16410-F1 | Checkpoint inhibitor target |
| RANKL (TNFSF11) | O14788 | AF-O14788-F1 | XGeva (denosumab) target |

### Workflow 3: De Novo Therapeutic Protein Design

For cancers where no existing drug targets the identified surface, design new proteins from scratch.

```
Target structure (AlphaFold or PDB)
  → Identify binding epitope (surface-exposed, tumor-specific)
  → RFdiffusion: generate backbone geometries that complement the epitope
  → ProteinMPNN: design amino acid sequences for each backbone
  → ESMFold / AlphaFold2: validate predicted structures (pLDDT >85, pTM >0.8)
  → Developability: assess aggregation, immunogenicity, expression
  → Top candidates → synthesis → experimental testing
```

**Pipeline tools:**
| Step | Tool | Stars | URL |
|------|------|-------|-----|
| Backbone generation | RFdiffusion | 2,808 | github.com/RosettaCommons/RFdiffusion |
| 2nd gen backbone | RFdiffusion2 | 408 | github.com/RosettaCommons/RFdiffusion2 |
| Sequence design | ProteinMPNN | 1,681 | github.com/dauparas/ProteinMPNN |
| Fast validation | ESMFold | - | Meta (via API) |
| High-accuracy validation | AlphaFold2 | - | DeepMind (local or ColabFold) |
| Protein-ligand | Chai/Boltz | - | For small molecule interactions |

### Workflow 4: Mutation Impact Analysis

Understand how each somatic mutation changes protein structure and function.

```
For each somatic mutation from WES/WGS:
  → Get wildtype protein sequence (UniProt)
  → Create mutant sequence
  → AlphaFold2: predict both structures
  → Compare: RMSD, pLDDT change, domain stability
  → Classify: destabilizing, surface-altering, or neutral
  → Surface-altering mutations on expressed proteins → potential neoantigen targets
  → Destabilizing mutations → may create misfolded protein → immune recognition
```

---

## Tool Stack Addition

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **AlphaFold2** | High-accuracy structure prediction | Validate neoantigen-MHC binding, analyze mutation impact |
| **AlphaFold Multimer** | Protein complex prediction | Peptide-MHC complexes, antibody-antigen interfaces |
| **ESMFold** | Fast single-chain prediction | Rapid screening of many candidates |
| **ESM-2** | Protein language model embeddings | Mutation effect prediction, sequence similarity |
| **RFdiffusion** | De novo backbone generation | Design custom tumor binders |
| **ProteinMPNN** | Sequence design for backbones | Optimize designed protein sequences |
| **Chai/Boltz** | Protein-ligand prediction | Radioligand-target binding analysis |
| **ColabFold** | Cloud AlphaFold with MSA server | Batch validation of many candidates |

---

## Quality Thresholds

| Metric | Good | Acceptable | Reject |
|--------|------|------------|--------|
| pLDDT (mean) | >85 | >75 | <70 |
| pTM | >0.80 | >0.70 | <0.65 |
| ipTM (complex) | >0.60 | >0.50 | <0.40 |
| PAE interface | <8 | <12 | >15 |
| MPNN score | >0.70 | >0.60 | <0.50 |

---

## What This Adds to the Framework

**Without structure**: "This mutation creates a peptide that MHCflurry predicts will bind HLA-A*02:01 with IC50=50nM."

**With structure**: "AlphaFold Multimer predicts this peptide-MHC complex forms a stable interface (ipTM=0.72, PAE=6.3) with the peptide anchored at P2 and P9 and the central residues solvent-exposed for TCR recognition. The neoantigen side chain at position P5 creates a novel surface not present in the wildtype — this is the structural basis for immune discrimination."

The structure-based approach provides mechanistic understanding, not just statistical prediction.
