import pandas as pd
import matplotlib.pyplot as plt
from gseapy import enrichr

# ---------------------------
# load DESeq2 results
# ---------------------------
df = pd.read_csv("GSE299876_ARPE_DESeq2_results.csv", index_col=0)
df['gene'] = df.index
df = df.dropna()

# significance threshold
sig = df[df['padj'] < 0.05]

# split directions
up = sig[sig['log2FoldChange'] > 0]['gene'].tolist()
down = sig[sig['log2FoldChange'] < 0]['gene'].tolist()

print("Up genes:", len(up))
print("Down genes:", len(down))

# ---------------------------
# export gene lists
# ---------------------------
with open("up_genes.txt", "w") as f:
    for g in up:
        f.write(g + "\n")

with open("down_genes.txt", "w") as f:
    for g in down:
        f.write(g + "\n")

print("Gene lists exported")


# ---------------------------
# enrichment function
# ---------------------------
def run_enrichment(gene_list, label):

    enr = enrichr(
        gene_list=gene_list,
        gene_sets='GO_Biological_Process_2021',
        organism='Human',
        outdir=None,
        cutoff=0.5
    )

    res = enr.results.sort_values("Adjusted P-value").head(10)
    res.to_csv(f"{label}_GO_enrichment.csv", index=False)
    return res


# run enrichment
up_res = run_enrichment(up, "UP")
down_res = run_enrichment(down, "DOWN")

# ---------------------------
# plot comparison
# ---------------------------
plt.figure(figsize=(7,5))

plt.scatter(up_res["Combined Score"], range(len(up_res)), label="UP", marker="o")
plt.scatter(down_res["Combined Score"], range(len(down_res)), label="DOWN", marker="s")

plt.yticks(range(len(up_res)), up_res["Term"])
plt.xlabel("Combined Score")
plt.title("Direction-Independent Program Enrichment")
plt.legend()
plt.tight_layout()

plt.savefig("Figure14_Direction_Independent_Pathways.png", dpi=300)

print("Figure14 created")
