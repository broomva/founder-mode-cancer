# founder-mode-pipeline

An Autoany (EGRI) project — evaluator-governed recursive improvement.

## Structure

```
founder-mode-pipeline/
├── problem-spec.yaml    # Problem definition
├── eval/                # Evaluator (immutable during trials)
│   └── run_eval.sh      # Evaluation script
├── artifacts/           # Mutable artifacts
├── ledger.jsonl         # Trial ledger (append-only)
└── harness/             # Execution harness
```

## Quick Start

1. Edit `problem-spec.yaml` to define your problem
2. Implement the evaluator in `eval/`
3. Place your baseline artifact in `artifacts/`
4. Run the evaluator on the baseline to get `baseline_score`
5. Begin the EGRI loop

## Core Law

> Do not grant an agent more mutation freedom than your evaluator can reliably judge.
