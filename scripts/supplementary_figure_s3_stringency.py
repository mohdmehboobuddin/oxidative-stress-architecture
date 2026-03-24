import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# Ensure supplementary directory exists
# --------------------------------------------------
os.makedirs("supplementary", exist_ok=True)

# --------------------------------------------------
# Load datasets
# --------------------------------------------------

# ARPE-19 microarray
arpe = pd.read_csv("DEG_gene_level.csv")

# iPSC-RPE nuclear RNA-seq
nuc = pd.read_csv(
    "GSE158909_supplementary/GSE158909_bxs-bxsh2o2_v29_nuc_DESeq_out_plusNAMES_CODING_GEO.txt",
    sep="\t"
)

# Clean RNA-seq
nuc = nuc.dropna(subset=["padj", "foldChange"]).copy()
nuc["log2FC"] = np.log2(nuc["foldChange"].replace(0, np.nan))

# --------------------------------------------------
# Stringency thresholds
# --------------------------------------------------
thresholds = [0.5, 1.0, 1.5, 2.0]
conserved_counts = []

# --------------------------------------------------
# Compute conserved genes per threshold
# --------------------------------------------------
for t in thresholds:
    arpe_sig = arpe[
        (arpe["FDR"] < 0.05) &
        (np.abs(arpe["log2FC"]) >= t)
    ]

    nuc_sig = nuc[
        (nuc["padj"] < 0.05) &
        (np.abs(nuc["log2FC"]) >= t)
    ]

    arpe_genes = set(arpe_sig["symbol"].dropna().unique())
    nuc_genes = set(nuc_sig["GeneName"].dropna().unique())

    conserved = arpe_genes.intersection(nuc_genes)
    conserved_counts.append(len(conserved))

# --------------------------------------------------
# Plot (NON-INTERACTIVE, SAFE)
# --------------------------------------------------
plt.figure(figsize=(7, 5))

plt.plot(
    thresholds,
    conserved_counts,
    marker="o",
    linewidth=2.5,
    color="navy"
)

plt.xlabel("|log2 Fold Change| Threshold", fontsize=11)
plt.ylabel("Number of Conserved Genes", fontsize=11)

plt.title(
    "Supplementary Figure S1: Stringency-Dependent\n"
    "Conservation of Oxidative Stress Genes",
    fontsize=12
)

plt.grid(alpha=0.3)
plt.tight_layout()

# --------------------------------------------------
# Save & close
# --------------------------------------------------
outpath = "supplementary/Supplementary_Figure_S1_Stringency_Conservation.png"
plt.savefig(outpath, dpi=300)
plt.close()

# --------------------------------------------------
# Confirmation
# --------------------------------------------------
print("✅ Supplementary Figure S1 generated successfully")
print("📄 Saved to:", outpath)
print("Thresholds:", thresholds)
print("Conserved gene counts:", conserved_counts)
