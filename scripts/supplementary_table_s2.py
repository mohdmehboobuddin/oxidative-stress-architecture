import pandas as pd
import gseapy as gp
import os

# -----------------------------
# Paths
# -----------------------------
OUTDIR = "supplementary"
os.makedirs(OUTDIR, exist_ok=True)

# -----------------------------
# Load conserved genes
# -----------------------------
genes = pd.read_csv(
    "Figure6_Conserved_OxStress_Genes.txt",
    header=None
)[0].dropna().unique().tolist()

print(f"Conserved genes used: {len(genes)}")

if len(genes) < 3:
    raise ValueError("Too few genes for enrichment")

# -----------------------------
# Run enrichment (GO + Reactome)
# -----------------------------
gene_sets = {
    "GO_Biological_Process_2021": "GO_Biological_Process",
    "Reactome_2022": "Reactome_Pathways"
}

all_results = []

for gs, label in gene_sets.items():
    print(f"Running enrichment: {gs}")

    enr = gp.enrichr(
        gene_list=genes,
        gene_sets=gs,
        organism="Human",
        outdir=None,
        cutoff=1.0,
        no_plot=True
    )

    if enr.results is None or enr.results.empty:
        print(f"⚠ No results for {gs}")
        continue

    res = enr.results.copy()
    res["Database"] = label
    all_results.append(res)

# -----------------------------
# Combine and save
# -----------------------------
if not all_results:
    raise ValueError("No enrichment results generated")

final_table = pd.concat(all_results, ignore_index=True)

# Clean column names
final_table = final_table.rename(columns={
    "Adjusted P-value": "Adjusted_P_value",
    "P-value": "P_value",
    "Odds Ratio": "Odds_Ratio",
    "Combined Score": "Combined_Score"
})

output_file = os.path.join(
    OUTDIR,
    "Supplementary_Table_S2_Functional_Enrichment.csv"
)

final_table.to_csv(output_file, index=False)

print("✅ Supplementary Table S2 generated successfully")
print(f"📄 Saved to: {output_file}")
print(f"📊 Rows × Columns: {final_table.shape}")
