import pandas as pd
from scipy.stats import fisher_exact

# Load conserved genes
with open("Figure6_Conserved_OxStress_Genes.txt") as f:
    conserved = set([line.strip() for line in f if line.strip()])

# Load DESeq2 results (gene names are row index)
deg = pd.read_csv("GSE299876_ARPE_DESeq2_results.csv", index_col=0)

# Adjusted p-value threshold
sig = deg[(deg['padj'] < 0.05) & (deg['log2FoldChange'].abs() > 0.5)]

deg_genes = set(sig.index.astype(str))

# Overlap
overlap = conserved & deg_genes

# Universe
all_genes = set(deg.index.astype(str))

# Fisher exact test
a = len(overlap)
b = len(conserved) - a
c = len(deg_genes) - a
d = len(all_genes) - (a+b+c)

oddsratio, pvalue = fisher_exact([[a,b],[c,d]])

print("Total conserved genes:", len(conserved))
print("Significant DEGs:", len(deg_genes))
print("Overlap:", a)
print("Fisher exact p-value:", pvalue)

# Save overlap list
with open("Validation_GSE299876_overlap_genes.txt","w") as f:
    for g in sorted(overlap):
        f.write(g+"\n")
