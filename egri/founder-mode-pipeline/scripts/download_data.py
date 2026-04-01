#!/usr/bin/env python3
"""
Phase 1: Download data from gs://osteosarc-genomics via HTTP.
No gsutil auth required — bucket is publicly readable.
"""
import os
import sys
import requests
from pathlib import Path

BASE = "https://storage.googleapis.com/osteosarc-genomics"
WORKDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("F:/founder-mode-pipeline")

FILES = {
    # T2 Mutect2 VCF (already VEP-annotated — skip Phase 2!)
    "data/variants/T2_mutect2_filtered_VEP.vcf.gz": (
        f"{BASE}/genomics_reprocessing/DNA/T2_2025_01_WGS_sarek_variants/annotation/mutect2/"
        "SG.WGS.UCLA.2025.01.tumor_vs_SG.WGS.UCLA.2024.06.06.normal/"
        "SG.WGS.UCLA.2025.01.tumor_vs_SG.WGS.UCLA.2024.06.06.normal.mutect2.filtered_VEP.ann.vcf.gz"
    ),
    # T1 Mutect2 VCF (VEP-annotated)
    "data/variants/T1_mutect2_filtered_VEP.vcf.gz": (
        f"{BASE}/genomics_reprocessing/DNA/T1_2024_WGS_sarek_variants/sarek_run1_tumor_normal_only/"
        "SG.WGS.UCLA.2024.06.06.tumor_vs_SG.WGS.UCLA.2024.06.06.normal.mutect2.filtered_VEP.ann.vcf.gz"
    ),
    # Existing pVACtools neoantigen predictions (for validation)
    "data/neoantigens/pvac_filtered.tsv": (
        f"{BASE}/neoantigen_prediction/pvactools/2025.04.25.sg.curated.neoantigen.predictions/"
        "MHC_Class_I/SG.WGS_SG.WGS.UCLA.2025.01.tumor.filtered.tsv"
    ),
    "data/neoantigens/pvac_all_epitopes.tsv": (
        f"{BASE}/neoantigen_prediction/pvactools/2025.04.25.sg.curated.neoantigen.predictions/"
        "MHC_Class_I/SG.WGS_SG.WGS.UCLA.2025.01.tumor.all_epitopes.tsv"
    ),
    "data/neoantigens/pvac_aggregated.tsv": (
        f"{BASE}/neoantigen_prediction/pvactools/2025.04.25.sg.curated.neoantigen.predictions/"
        "MHC_Class_I/SG.WGS_SG.WGS.UCLA.2025.01.tumor.all_epitopes.aggregated.tsv"
    ),
    "data/neoantigens/pvac_peptides.fasta": (
        f"{BASE}/neoantigen_prediction/pvactools/2025.04.25.sg.curated.neoantigen.predictions/"
        "MHC_Class_I/SG.WGS_SG.WGS.UCLA.2025.01.tumor.fasta"
    ),
    "data/neoantigens/pvac_config.yml": (
        f"{BASE}/neoantigen_prediction/pvactools/2025.04.25.sg.curated.neoantigen.predictions/"
        "MHC_Class_I/log/inputs.yml"
    ),
    # RNA-seq gene expression (UCLA 2025 — most recent)
    "data/rnaseq/SARC0277_gene_tpm.gct.gz": (
        f"{BASE}/rna-seq/reprocessed/SARC0277/SARC0277.gene_tpm.gct.gz"
    ),
    # T1 raw count matrix (for scRNA-seq fallback)
    "data/scrna/T1_rawmatrix.txt": (
        f"{BASE}/ucsf/T1/biopsy_06_2024_rawmatrix.txt"
    ),
}

# Large file: T1 Seurat RDS (969 MB) — download separately
LARGE_FILES = {
    "data/scrna/T1_seurat_annotated.rds": (
        f"{BASE}/ucsf/misc_seurat_loupe_objects/src044_for_pfo/"
        "072925_IPISRC044_T1_scrna_live_res1.2_processed_annot_allAnnot_tcr_clonotype.rds"
    ),
}


def download_file(url, dest, chunk_size=8192):
    dest = WORKDIR / dest
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        print(f"  SKIP (exists): {dest.name}")
        return True

    print(f"  Downloading: {dest.name} ...", end=" ", flush=True)
    try:
        resp = requests.get(url, stream=True, timeout=600)
        resp.raise_for_status()
        total = int(resp.headers.get("content-length", 0))
        downloaded = 0
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                downloaded += len(chunk)
        size_mb = downloaded / (1024 * 1024)
        print(f"OK ({size_mb:.1f} MB)")
        return True
    except Exception as e:
        print(f"FAILED: {e}")
        if dest.exists():
            dest.unlink()
        return False


def main():
    print(f"=== Phase 1: Data Acquisition ===")
    print(f"Workdir: {WORKDIR}")
    print(f"Downloading {len(FILES)} small files + {len(LARGE_FILES)} large files\n")

    success = 0
    failed = 0

    print("--- Small files ---")
    for dest, url in FILES.items():
        if download_file(url, dest):
            success += 1
        else:
            failed += 1

    print("\n--- Large files (scRNA-seq Seurat) ---")
    for dest, url in LARGE_FILES.items():
        if download_file(url, dest, chunk_size=65536):
            success += 1
        else:
            failed += 1

    print(f"\n=== Summary: {success} downloaded, {failed} failed ===")

    # Verify
    print("\nFile inventory:")
    for d in ["data/variants", "data/neoantigens", "data/rnaseq", "data/scrna"]:
        full = WORKDIR / d
        if full.exists():
            files = list(full.iterdir())
            total_mb = sum(f.stat().st_size for f in files if f.is_file()) / (1024 * 1024)
            print(f"  {d}/: {len(files)} files, {total_mb:.1f} MB")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
