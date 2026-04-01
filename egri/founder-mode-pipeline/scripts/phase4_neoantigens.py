#!/usr/bin/env python3
"""
Phase 4: Use existing pVACtools predictions from osteosarc.com.
Extract top 50 candidates for structural validation.
"""
import sys
import pandas as pd
from pathlib import Path

WORKDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("F:/founder-mode-pipeline")

neo_dir = WORKDIR / "data" / "neoantigens"
results = WORKDIR / "results" / "neoantigens"
results.mkdir(parents=True, exist_ok=True)

# Load all epitopes
all_epitopes = neo_dir / "pvac_all_epitopes.tsv"
filtered = neo_dir / "pvac_filtered.tsv"

print("=== Phase 4: Neoantigen Prediction (using existing pVACtools output) ===")

if all_epitopes.exists():
    df = pd.read_csv(str(all_epitopes), sep="\t")
    print(f"All epitopes: {len(df)} rows")
    print(f"Unique genes: {df['Gene Name'].nunique()}")
    print(f"HLA alleles: {sorted(df['HLA Allele'].unique())}")
    print(f"Peptide lengths: {sorted(df['Peptide Length'].unique())}")

    # Top 50 by binding affinity
    top50 = df.nsmallest(50, "Best MT IC50 Score")
    top50.to_csv(str(results / "top50_candidates.csv"), index=False)

    print(f"\nTop 50 candidates saved. Range: IC50 {top50['Best MT IC50 Score'].min():.1f} - {top50['Best MT IC50 Score'].max():.1f} nM")
    print(f"\nTop 20:")
    for i, (_, r) in enumerate(top50.head(20).iterrows()):
        print(f"  {i+1:2d}. {r['Gene Name']:12s} {r['MT Epitope Seq']:15s} IC50={r['Best MT IC50 Score']:7.1f}nM HLA={r['HLA Allele']}")

    # Save peptides for ESMFold
    peptides = top50["MT Epitope Seq"].unique()
    with open(str(results / "top50_peptides.txt"), "w") as f:
        for p in peptides:
            f.write(p + "\n")
    print(f"\n{len(peptides)} unique peptides saved for structural validation")

if filtered.exists():
    filt = pd.read_csv(str(filtered), sep="\t")
    print(f"\nFiltered candidates (from osteosarc.com): {len(filt)}")
    for _, r in filt.iterrows():
        print(f"  {r['Gene Name']:12s} {r['MT Epitope Seq']:15s} IC50={r['Best MT IC50 Score']:7.1f}nM HLA={r['HLA Allele']}")

print("\n=== Phase 4 COMPLETE ===")
