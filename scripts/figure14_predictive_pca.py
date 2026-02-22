import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# load expression matrix you previously used for PCA
# (the same dataset that produced Figure3_PCA_OxidativeStress.png)
expr = pd.read_csv("DEG_gene_level.csv", index_col=0)

# load conserved genes
with open("Figure6_Conserved_OxStress_Genes.txt") as f:
    conserved = [x.strip() for x in f if x.strip()]

# keep only conserved genes present in dataset
expr = expr.loc[expr.index.intersection(conserved)]

# transpose: samples as rows
X = expr.T

# scale
X_scaled = StandardScaler().fit_transform(X)

# PCA
pca = PCA(n_components=2)
pc = pca.fit_transform(X_scaled)

# determine groups from sample names
labels = ["Stress" if "stress" in s.lower() else "Control" for s in X.index]

# plot
plt.figure(figsize=(6,5))
for i,label in enumerate(labels):
    if label=="Stress":
        plt.scatter(pc[i,0],pc[i,1],color="red")
    else:
        plt.scatter(pc[i,0],pc[i,1],color="blue")

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Sample Separation Using Only Conserved Oxidative Stress Genes")
plt.tight_layout()
plt.savefig("Figure14_Predictive_PCA.png",dpi=300)

print("Predictive PCA figure created")
