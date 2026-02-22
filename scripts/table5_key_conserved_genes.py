import pandas as pd
import numpy as np

# -------------------------------
# Load conserved genes
# -------------------------------
genes = pd.read_csv(
    "Figure6_Conserved_OxStress_Genes.txt",
    header=None
)[0].dropna().unique().tolist()

print("Conserved genes used:", len(genes))

# -------------------------------
# Load ARPE-19 microarray data
# -------------------------------
arpe = pd.read_csv("DEG_gene_level.csv")

arpe = arpe.rename(columns={
    "symbol": "Gene",
    "log2FC": "ARPE_log2FC"
})

arpe = arpe[arpe["Gene"].isin(genes)]
arpe = arpe.groupby("Gene", as_index=False)["ARPE_log2FC"].mean()

# -------------------------------
# Load iPSC-RPE RNA-seq data
# -------------------------------
nuc = pd.read_csv(
    "GSE158909_supplementary/GSE158909_bxs-bxsh2o2_v29_nuc_DESeq_out_plusNAMES_CODING_GEO.txt",
    sep="\t"
)

nuc = nuc.dropna(subset=["foldChange"]).copy()
nuc["iPSC_log2FC"] = np.log2(nuc["foldChange"].replace(0, np.nan))

nuc = nuc.rename(columns={"GeneName": "Gene"})
nuc = nuc[nuc["Gene"].isin(genes)]
nuc = nuc.groupby("Gene", as_index=False)["iPSC_log2FC"].mean()

# -------------------------------
# Merge datasets
# -------------------------------
table5 = pd.merge(arpe, nuc, on="Gene", how="inner")

# -------------------------------
# Direction consistency
# -------------------------------
def direction(row):
    if row["ARPE_log2FC"] * row["iPSC_log2FC"] > 0:
        return "Concordant"
    else:
        return "Discordant"

table5["Direction_Consistency"] = table5.apply(direction, axis=1)

# -------------------------------
# Functional annotation (manual, reviewer-grade)
# -------------------------------
functional_roles = {
    "LMNA": "Nuclear structure and stress-responsive chromatin organization",
    "BRD4": "Transcriptional regulation and oxidative stress signaling",
    "EIF4G1": "Cap-dependent translation during stress adaptation",
    "GANAB": "Protein folding and ER stress regulation",
    "ITGA3": "Cell adhesion and epithelial integrity",
    "MBOAT7": "Membrane lipid remodeling and redox balance",
    "NSD2": "Epigenetic regulation of stress-responsive genes",
    "PTPRF": "Receptor signaling and redox-sensitive phosphatase activity",
    "SLC2A1": "Glucose transport and metabolic stress adaptation",
    "SMARCA4": "Chromatin remodeling under oxidative stress",
    "STAT2": "Interferon and redox-linked transcriptional signaling",
    "WDR1": "Actin cytoskeleton dynamics during cellular stress"
}

table5["Functional_Role"] = table5["Gene"].map(functional_roles)

# -------------------------------
# Evidence level
# -------------------------------
table5["Evidence_Level"] = "Transcriptomic + Functional"

# -------------------------------
# Final formatting
# -------------------------------
table5 = table5.rename(columns={
    "ARPE_log2FC": "ARPE-19_log2FC",
    "iPSC_log2FC": "iPSC-RPE_log2FC"
})

table5 = table5.sort_values(
    by=["Direction_Consistency", "ARPE-19_log2FC"],
    ascending=[True, False]
)

# -------------------------------
# Save table
# -------------------------------
table5.to_csv("Table5_Key_Conserved_OxStress_Genes.csv", index=False)

print("\n✅ Table 5 generated successfully")
print(table5)
