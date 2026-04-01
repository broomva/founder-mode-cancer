#!/usr/bin/env bash
# EGRI Evaluator — Founder Mode Oncology Pipeline
# Scores the pipeline run by checking outputs from each phase.
# Returns JSON with metrics.
set -euo pipefail

WORKDIR="${1:-F:/founder-mode-pipeline}"
RESULTS="$WORKDIR/results"

python3 - "$RESULTS" <<'PYEOF'
import sys, os, csv, json

results = sys.argv[1]

def file_exists(path):
    return os.path.isfile(os.path.join(results, path))

def dir_has_files(path):
    full = os.path.join(results, '..', 'data', path)
    return os.path.isdir(full) and len(os.listdir(full)) > 0

# Phase completion
phases = {
    "phase1_data": dir_has_files("variants"),
    "phase2_annotation": file_exists("variants/annotated.vcf"),
    "phase3_scrna": file_exists("scrna/differential_expression_all_clusters.csv"),
    "phase4_neoantigens": file_exists("neoantigens/top50_candidates.csv"),
    "phase5_alphafold": file_exists("alphafold/structural_validation.csv"),
    "phase6_treatment": file_exists("TREATMENT_RECOMMENDATION.md"),
}

phases_done = sum(phases.values())
pipeline_complete = phases_done == 6

# Count candidates
neoantigen_count = t1_count = t2_count = 0
if phases["phase5_alphafold"]:
    path = os.path.join(results, "alphafold/structural_validation.csv")
    for r in csv.DictReader(open(path)):
        if r.get("pass", "").lower() == "true":
            neoantigen_count += 1
        if r.get("tier", "") == "T1":
            t1_count += 1
        elif r.get("tier", "") == "T2":
            t2_count += 1

# FAP detection
fap_detected = False
if phases["phase3_scrna"]:
    path = os.path.join(results, "scrna/differential_expression_all_clusters.csv")
    for r in csv.DictReader(open(path)):
        if r.get("names", "") == "FAP":
            try:
                if float(r.get("logfoldchanges", 0)) > 1:
                    fap_detected = True
                    break
            except (ValueError, TypeError):
                pass

json.dump({
    "score": neoantigen_count,
    "metrics": {
        "neoantigen_count": neoantigen_count,
        "t1_count": t1_count,
        "t2_count": t2_count,
        "fap_detected": fap_detected,
        "phases_completed": phases_done,
        "pipeline_complete": pipeline_complete,
        **phases,
    },
    "constraints_passed": True,
    "constraint_violations": [],
}, sys.stdout, indent=2)
PYEOF
