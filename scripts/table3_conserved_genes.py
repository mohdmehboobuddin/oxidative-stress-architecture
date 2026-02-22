# ================================
# Table 3: Conserved Oxidative Stress Genes
# ================================

import pandas as pd
import numpy as np

# -------------------------------
# Load conserved gene list
# -------------------------------
genes = (
    pd.read_csv("Figure6_Conserved_OxStress_Genes.txt", header=None)[0]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

print("Total conserved genes (input):", len(genes))

# -------------------------------
# Load ARPE-19 DEG results
# -------------------------------
arpe = pd.read_csv("DEG_gene_level.csv")

# Safety checks
if "symbol" not in arpe.columns or "log2FC" not in arpe.columns:
    raise ValueError("ARPE DEG file must contain 'symbol' and 'log2FC' columns")

arpe_gene = (
    arpe[arpe["symbol"].isin(genes)]
    .groupby("symbol", as_index=False)
    .agg({"log2FC": "mean"})
    .rename(columns={"symbol": "Gene", "log2FC": "ARPE-19_log2FC"})
)

# -------------------------------
# Load iPSC-RPE nuclear RNA-seq
# -------------------------------
nuc = pd.read_csv(
    "GSE158909_supplementary/GSE158909_bxs-bxsh2o2_v29_nuc_DESeq_out_plusNAMES_CODING_GEO.txt",
    sep="\t"
)

# Detect fold-change column safely
if "foldChange" not in nuc.columns:
    raise ValueError("RNA-seq file must contain 'foldChange' column")

nuc = nuc.dropna(subset=["GeneName", "foldChange"]).copy()
nuc["log2FC"] = np.log2(nuc["foldChange"].replace(0, np.nan))

# Remove infinities explicitly
nuc = nuc.replace([np.inf, -np.inf], np.nan)

nuc_gene = (
    nuc[nuc["GeneName"].isin(genes)]
    .groupby("GeneName", as_index=False)
    .agg({"log2FC": "mean"})
    .rename(columns={"GeneName": "Gene", "log2FC": "iPSC-RPE_log2FC"})
)

# -------------------------------
# Merge datasets
# -------------------------------
table3 = pd.merge(
    arpe_gene,
    nuc_gene,
    on="Gene",
    how="outer"
)

# -------------------------------
# Direction consistency logic
# -------------------------------
def consistency(row):
    if pd.isna(row["ARPE-19_log2FC"]) or pd.isna(row["iPSC-RPE_log2FC"]):
        return "Not Available"
    if row["ARPE-19_log2FC"] * row["iPSC-RPE_log2FC"] > 0:
        return "Concordant"
    else:
        return "Discordant"

table3["Direction_Consistency"] = table3.apply(consistency, axis=1)

# -------------------------------
# Final cleanup
# -------------------------------
table3 = table3.sort_values(
    by=["Direction_Consistency", "Gene"],
    ascending=[True, True]
).reset_index(drop=True)

# -------------------------------
# Save table
# -------------------------------
table3.to_csv("Table3_Conserved_OxStress_Genes.csv", index=False)

print("✅ Table 3 generated successfully")
print(table3)
