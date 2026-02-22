import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gseapy as gp

# ----------------------------
# Load conserved gene list
# ----------------------------
genes = pd.read_csv(
    "Figure6_Conserved_OxStress_Genes.txt",
    header=None
)[0].dropna().unique().tolist()

print("Genes used:", len(genes))

# ----------------------------
# Run enrichment
# ----------------------------
enr = gp.enrichr(
    gene_list=genes,
    gene_sets=[
        "GO_Biological_Process_2021",
        "Reactome_2022"
    ],
    organism="Human",
    outdir=None,
    cutoff=1.0,
    no_plot=True
)

res = enr.results.sort_values("Adjusted P-value")

# Save full table
res.to_csv(
    "supplementary/Supplementary_Figure_S3_Pathway_Results.csv",
    index=False
)

# ----------------------------
# Plot top 12 pathways
# ----------------------------
top = res.head(12)

plt.figure(figsize=(9, 6))

plt.barh(
    top["Term"],
    -np.log10(top["Adjusted P-value"]),
    color="#2E8B57"
)

plt.xlabel("-log10 Adjusted P-value")
plt.title(
    "Supplementary Figure S3: Functional Enrichment of\n"
    "Conserved Oxidative Stress Genes (Relaxed Set)"
)

plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig(
    "supplementary/Supplementary_Figure_S3_Pathway_Enrichment.png",
    dpi=300
)
plt.close()

print("✅ Supplementary Figure S3 generated successfully")
