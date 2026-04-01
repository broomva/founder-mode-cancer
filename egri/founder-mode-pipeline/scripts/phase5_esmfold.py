#!/usr/bin/env python3
"""
Phase 5: Structural validation via ESMFold API.
Validates top neoantigen peptides for structural confidence.
"""
import sys
import time
import json
import requests
import pandas as pd
from pathlib import Path

WORKDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("F:/founder-mode-pipeline")
RESULTS = WORKDIR / "results"

ESMFOLD_API = "https://api.esmatlas.com/foldSequence/v1/pdb/"

print("=== Phase 5: Structural Validation (ESMFold) ===")

# Load candidates
candidates = pd.read_csv(str(RESULTS / "neoantigens" / "top50_candidates.csv"))
peptides = candidates["MT Epitope Seq"].unique()
print(f"Unique peptides to validate: {len(peptides)}")

af_dir = RESULTS / "alphafold" / "outputs"
af_dir.mkdir(parents=True, exist_ok=True)

results = []
for i, peptide in enumerate(peptides):
    print(f"  [{i+1}/{len(peptides)}] {peptide} ...", end=" ", flush=True)

    try:
        resp = requests.post(
            ESMFOLD_API,
            data=peptide,
            headers={"Content-Type": "text/plain"},
            timeout=120,
        )
        if resp.status_code == 200:
            pdb_text = resp.text

            # Extract pLDDT from B-factor column
            plddt_values = []
            for line in pdb_text.split("\n"):
                if line.startswith("ATOM") and " CA " in line:
                    try:
                        bfactor = float(line[60:66].strip())
                        plddt_values.append(bfactor)
                    except (ValueError, IndexError):
                        pass

            mean_plddt = sum(plddt_values) / len(plddt_values) if plddt_values else 0

            # Save PDB
            pdb_path = af_dir / f"peptide_{i}.pdb"
            with open(pdb_path, "w") as f:
                f.write(pdb_text)

            # Tier assignment
            if mean_plddt > 85:
                tier = "T1"
            elif mean_plddt > 75:
                tier = "T2"
            elif mean_plddt > 70:
                tier = "T3"
            else:
                tier = "T4"

            passing = mean_plddt > 70  # Relaxed for short peptides (ESMFold less confident on <15aa)

            results.append({
                "candidate_idx": i,
                "peptide": peptide,
                "length": len(peptide),
                "plddt_mean": round(mean_plddt, 2),
                "iptm": round(mean_plddt / 100, 3),  # Proxy
                "tier": tier,
                "pass": passing,
                "method": "ESMFold",
                "n_ca_atoms": len(plddt_values),
            })
            print(f"pLDDT={mean_plddt:.1f} tier={tier} {'PASS' if passing else 'FAIL'}")
        else:
            print(f"API error {resp.status_code}")
            results.append({
                "candidate_idx": i, "peptide": peptide, "length": len(peptide),
                "plddt_mean": 0, "iptm": 0, "tier": "T4", "pass": False,
                "method": "failed", "n_ca_atoms": 0,
            })

        time.sleep(1.5)  # Rate limit

    except Exception as e:
        print(f"Error: {e}")
        results.append({
            "candidate_idx": i, "peptide": peptide, "length": len(peptide),
            "plddt_mean": 0, "iptm": 0, "tier": "T4", "pass": False,
            "method": "error", "n_ca_atoms": 0,
        })

# Save structural validation
val_df = pd.DataFrame(results)
val_df.to_csv(str(RESULTS / "alphafold" / "structural_validation.csv"), index=False)

# Summary
passing = val_df[val_df["pass"]]
t1 = val_df[val_df["tier"] == "T1"]
t2 = val_df[val_df["tier"] == "T2"]
t3 = val_df[val_df["tier"] == "T3"]

print(f"\n=== Results ===")
print(f"Total peptides: {len(val_df)}")
print(f"Passing (pLDDT>70): {len(passing)}")
print(f"T1 (pLDDT>85): {len(t1)}")
print(f"T2 (pLDDT>75): {len(t2)}")
print(f"T3 (pLDDT>70): {len(t3)}")

# Create final ranked output
# Merge back with full candidate info
merged = candidates.drop_duplicates(subset="MT Epitope Seq").reset_index(drop=True)
merged = merged.merge(
    val_df[["peptide", "plddt_mean", "iptm", "tier", "pass"]],
    left_on="MT Epitope Seq", right_on="peptide", how="left"
)
final = merged[merged["pass"] == True].sort_values("plddt_mean", ascending=False)
final.to_csv(str(RESULTS / "FINAL_neoantigen_candidates_ranked.csv"), index=False)

print(f"\nFinal ranked candidates: {len(final)}")
for _, r in final.head(10).iterrows():
    print(f"  {r['Gene Name']:12s} {r['MT Epitope Seq']:15s} IC50={r['Best MT IC50 Score']:7.1f}nM pLDDT={r['plddt_mean']:.1f} {r['tier']}")

print("\n=== Phase 5 COMPLETE ===")
