import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

# load conserved genes
with open("Figure6_Conserved_OxStress_Genes.txt") as f:
    conserved = set([line.strip() for line in f if line.strip()])

# load DESeq2
deg = pd.read_csv("GSE299876_ARPE_DESeq2_results.csv", index_col=0)

deg['absLFC'] = deg['log2FoldChange'].abs()

conserved_scores = deg.loc[deg.index.isin(conserved), 'absLFC']
background_scores = deg.loc[~deg.index.isin(conserved), 'absLFC']

stat, pvalue = mannwhitneyu(conserved_scores, background_scores, alternative='greater')

print("Median LFC conserved:", np.median(conserved_scores))
print("Median LFC background:", np.median(background_scores))
print("Enrichment p-value:", pvalue)
