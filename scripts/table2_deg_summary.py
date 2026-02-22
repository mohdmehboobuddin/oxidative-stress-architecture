import pandas as pd
import numpy as np

# ============================
# ARPE-19 MICROARRAY
# ============================
arpe = pd.read_csv("DEG_gene_level.csv")

arpe_up = ((arpe["FDR"] < 0.05) & (arpe["log2FC"] > 0)).sum()
arpe_down = ((arpe["FDR"] < 0.05) & (arpe["log2FC"] < 0)).sum()

# ============================
# iPSC-RPE NUCLEAR RNA-seq
# ============================
nuc = pd.read_csv(
    "GSE158909_supplementary/"
    "GSE158909_bxs-bxsh2o2_v29_nuc_DESeq_out_plusNAMES_CODING_GEO.txt",
    sep="\t"
)

# --- compute log2FC from foldChange ---
if "foldChange" not in nuc.columns:
    raise ValueError("foldChange column not found in RNA-seq file")

nuc["log2FC"] = np.log2(nuc["foldChange"].replace(0, np.nan))

# --- adjusted p-value ---
if "padj" not in nuc.columns:
    raise ValueError("padj column not found in RNA-seq file")

nuc_up = ((nuc["padj"] < 0.05) & (nuc["log2FC"] > 0)).sum()
nuc_down = ((nuc["padj"] < 0.05) & (nuc["log2FC"] < 0)).sum()

# ============================
# TABLE 2
# ============================
table2 = pd.DataFrame([
    {
        "Dataset": "GSE122270",
        "Technology": "Agilent Microarray (ARPE-19)",
        "Upregulated Genes": arpe_up,
        "Downregulated Genes": arpe_down,
        "Total DEGs": arpe_up + arpe_down
    },
    {
        "Dataset": "GSE158909",
        "Technology": "Nuclear RNA-seq (iPSC-RPE)",
        "Upregulated Genes": nuc_up,
        "Downregulated Genes": nuc_down,
        "Total DEGs": nuc_up + nuc_down
    }
])

table2.to_csv(
    "Table2_Differential_Expression_Summary.csv",
    index=False
)

print("\n✅ Table 2 generated successfully:\n")
print(table2)
