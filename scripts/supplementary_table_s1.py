import pandas as pd
import numpy as np
import os

# -------------------------------------------------
# Ensure supplementary directory exists
# -------------------------------------------------
os.makedirs("supplementary", exist_ok=True)

# -------------------------------------------------
# Load ARPE-19 microarray DEG data
# -------------------------------------------------
arpe = pd.read_csv("DEG_gene_level.csv")

# Check required columns
required_arpe_cols = {"symbol", "log2FC", "FDR"}
missing = required_arpe_cols - set(arpe.columns)
if missing:
    raise ValueError(f"Missing columns in DEG_gene_level.csv: {missing}")

arpe_sup = arpe[["symbol", "log2FC", "FDR"]].copy()
arpe_sup.rename(columns={
    "symbol": "Gene",
    "FDR": "Adjusted_P_Value"
}, inplace=True)

arpe_sup["Dataset"] = "GSE122270 (ARPE-19 Microarray)"

# -------------------------------------------------
# Load iPSC-RPE nuclear RNA-seq data
# -------------------------------------------------
nuc = pd.read_csv(
    "GSE158909_supplementary/GSE158909_bxs-bxsh2o2_v29_nuc_DESeq_out_plusNAMES_CODING_GEO.txt",
    sep="\t"
)

# Compute log2FC safely
nuc = nuc.dropna(subset=["foldChange"])
nuc["log2FC"] = np.log2(nuc["foldChange"].replace(0, np.nan))

nuc_sup = nuc[["GeneName", "log2FC"]].copy()
nuc_sup.rename(columns={"GeneName": "Gene"}, inplace=True)

# RNA-seq adjusted p-values not merged here (kept NA)
nuc_sup["Adjusted_P_Value"] = np.nan
nuc_sup["Dataset"] = "GSE158909 (iPSC-RPE Nuclear RNA-seq)"

# -------------------------------------------------
# Combine into Supplementary Table S1
# -------------------------------------------------
supp_table_s1 = pd.concat(
    [arpe_sup, nuc_sup],
    ignore_index=True
)

# Save table
output_file = "supplementary/Supplementary_Table_S1_Full_DEG_List.csv"
supp_table_s1.to_csv(output_file, index=False)

# -------------------------------------------------
# Report
# -------------------------------------------------
print("✅ Supplementary Table S1 generated successfully")
print("📄 Saved to:", output_file)
print("📊 Rows × Columns:", supp_table_s1.shape)
