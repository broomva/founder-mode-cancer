#!/usr/bin/env python3
"""
Phase 3: scRNA-seq Target Discovery
Uses T1 raw count matrix to identify non-obvious surface targets (FAP, B7H3, EphA2).
"""
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("phase3")

WORKDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("F:/founder-mode-pipeline")
DATA = WORKDIR / "data" / "scrna"
RESULTS = WORKDIR / "results" / "scrna"
RESULTS.mkdir(parents=True, exist_ok=True)

TARGET_GENES = [
    "FAP", "CD276", "EPHA2", "MSLN", "FOLR1", "MUC1",
    "ERBB2", "EGFR", "MET", "PDGFRA", "KIT", "PDCD1",
    "CD274", "CTLA4", "HAVCR2", "LAG3", "TIGIT",
]


def load_data():
    """Try multiple data formats."""
    import scanpy as sc
    import pandas as pd

    # Option 1: Raw count matrix (tab-separated, genes x cells)
    raw_matrix = DATA / "T1_rawmatrix.txt"
    if raw_matrix.exists():
        log.info(f"Loading raw matrix: {raw_matrix} ({raw_matrix.stat().st_size / 1e6:.0f} MB)")
        try:
            # Try reading as genes (rows) x cells (columns)
            df = pd.read_csv(str(raw_matrix), sep="\t", index_col=0)
            log.info(f"  Raw shape: {df.shape}")
            if df.shape[0] > df.shape[1]:
                # Genes as rows, cells as columns — transpose
                log.info("  Transposing (genes x cells → cells x genes)")
                adata = sc.AnnData(df.T)
            else:
                adata = sc.AnnData(df)
            log.info(f"  AnnData: {adata.n_obs} cells x {adata.n_vars} genes")
            return adata
        except Exception as e:
            log.warning(f"  Failed to load as TSV: {e}")

    # Option 2: H5AD
    for h5ad in DATA.glob("*.h5ad"):
        log.info(f"Loading H5AD: {h5ad}")
        return sc.read_h5ad(str(h5ad))

    # Option 3: 10x H5
    for h5 in DATA.glob("*.h5"):
        log.info(f"Loading 10x H5: {h5}")
        return sc.read_10x_h5(str(h5))

    return None


def run_analysis(adata):
    """Standard Scanpy pipeline + target discovery."""
    import scanpy as sc
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")

    log.info("Starting Scanpy analysis...")

    # QC
    log.info("QC filtering...")
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)

    # MT genes
    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    if adata.var["mt"].sum() > 0:
        sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)
        n_before = adata.n_obs
        adata = adata[adata.obs.pct_counts_mt < 20, :].copy()
        log.info(f"  MT filter: {n_before} → {adata.n_obs} cells")
    log.info(f"After QC: {adata.n_obs} cells x {adata.n_vars} genes")

    # Normalize
    log.info("Normalizing...")
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    adata.raw = adata

    # HVG
    sc.pp.highly_variable_genes(adata, n_top_genes=3000)
    adata = adata[:, adata.var.highly_variable].copy()

    # PCA + neighbors + UMAP
    log.info("Dimensionality reduction...")
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver="arpack")
    sc.pp.neighbors(adata, n_neighbors=15, n_pcs=min(40, adata.n_obs - 1))
    sc.tl.umap(adata)

    # Clustering
    log.info("Clustering...")
    sc.tl.leiden(adata, resolution=0.8)
    n_clusters = adata.obs["leiden"].nunique()
    log.info(f"Found {n_clusters} clusters")

    # Differential expression
    log.info("Differential expression...")
    sc.tl.rank_genes_groups(adata, "leiden", method="wilcoxon")
    de_df = sc.get.rank_genes_groups_df(adata, group=None)
    de_df.to_csv(str(RESULTS / "differential_expression_all_clusters.csv"), index=False)
    log.info(f"DE results: {len(de_df)} gene-cluster combinations")

    # Target discovery
    log.info("=" * 50)
    log.info("TARGET DISCOVERY")
    log.info("=" * 50)

    available_targets = [g for g in TARGET_GENES if g in adata.raw.var_names]
    missing_targets = [g for g in TARGET_GENES if g not in adata.raw.var_names]
    log.info(f"Available targets: {len(available_targets)}/{len(TARGET_GENES)}")
    if missing_targets:
        log.info(f"Missing: {', '.join(missing_targets)}")

    target_results = []
    for gene in available_targets:
        gene_de = de_df[de_df["names"] == gene]
        if not gene_de.empty:
            best = gene_de.sort_values("logfoldchanges", ascending=False).iloc[0]
            is_sig = bool(best["logfoldchanges"] > 1 and best["pvals_adj"] < 0.05)
            target_results.append({
                "gene": gene,
                "best_cluster": best["group"],
                "log2fc": round(float(best["logfoldchanges"]), 3),
                "pval_adj": float(best["pvals_adj"]),
                "significant": is_sig,
            })
            marker = "***" if is_sig else "   "
            log.info(f"  {marker} {gene}: log2FC={best['logfoldchanges']:.2f}, padj={best['pvals_adj']:.2e}, cluster={best['group']}")

    targets_df = pd.DataFrame(target_results)
    targets_df.to_csv(str(RESULTS / "target_discovery_summary.csv"), index=False)

    sig_targets = targets_df[targets_df["significant"]]
    log.info(f"\nSignificant targets (log2FC>1, padj<0.05): {len(sig_targets)}")
    for _, row in sig_targets.iterrows():
        log.info(f"  {row['gene']}: log2FC={row['log2fc']}, cluster={row['best_cluster']}")

    # FAP specific check
    fap_sig = "FAP" in sig_targets["gene"].values if not sig_targets.empty else False
    log.info(f"\nFAP OVEREXPRESSION: {'CONFIRMED' if fap_sig else 'NOT DETECTED'}")

    # Save plots
    log.info("Generating plots...")
    sc.settings.figdir = str(RESULTS)
    try:
        sc.pl.umap(adata, color=["leiden"], save="_clusters.png", show=False)
        if available_targets:
            sc.pl.dotplot(
                adata.raw.to_adata(), available_targets,
                groupby="leiden", save="_target_discovery.png", show=False
            )
    except Exception as e:
        log.warning(f"Plot generation failed (non-fatal): {e}")

    # Save processed data
    log.info("Saving processed data...")
    adata.write(str(RESULTS / "analyzed_tumor.h5ad"))

    # Summary
    log.info("=" * 50)
    log.info("PHASE 3 COMPLETE")
    log.info(f"  Cells: {adata.n_obs}")
    log.info(f"  Clusters: {n_clusters}")
    log.info(f"  Significant targets: {len(sig_targets)}")
    log.info(f"  FAP detected: {fap_sig}")
    log.info("=" * 50)

    return True


def main():
    adata = load_data()
    if adata is None:
        log.error("No scRNA-seq data could be loaded!")
        sys.exit(1)

    success = run_analysis(adata)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
