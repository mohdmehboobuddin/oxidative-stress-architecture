import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gseapy as gp

# Load conserved genes
genes = pd.read_csv(
    "Figure6_Conserved_OxStress_Genes.txt",
    header=None
)[0].dropna().unique().tolist()

print("Genes used for GO enrichment:", len(genes))

# Run GO enrichment
enr = gp.enrichr(
    gene_list=genes,
    gene_sets="GO_Biological_Process_2021",
    organism="Human",
    outdir=None,
    cutoff=1.0,
    no_plot=True
)

# Sort results
res = enr.results.sort_values("Adjusted P-value")
print("Total GO terms found:", res.shape[0])

# Select top 9
top9 = res.head(9)

# Save table
res.to_csv("Figure7A_GO_Full_Results.csv", index=False)

# Plot
plt.figure(figsize=(9, 6))
plt.barh(
    top9["Term"],
    -np.log10(top9["Adjusted P-value"]),
    color="steelblue"
)

plt.xlabel("-log10 Adjusted P-value")
plt.title(
    "Figure 7A: Functional Enrichment of Conserved\n"
    "Oxidative Stress Genes Across Human Epithelial Cells"
)

plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("Figure7A_GO_Functional_Enrichment_TOP9.png", dpi=300)
plt.show()

print("Figure 7A generated successfully")
