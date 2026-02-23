import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# -----------------------------
# load count matrix
# -----------------------------
df = pd.read_csv("validation_datasets/GSE299876/GSE299876_ARPE_count_matrix.csv")

df = df.set_index("Gene")

# samples
ctrl = [c for c in df.columns if "Ctrl" in c]
stress = [c for c in df.columns if "H2O2" in c]

samples = ctrl + stress

data = df[samples]

# -----------------------------
# load conserved genes
# -----------------------------
genes = [g.strip() for g in open("Figure6_Conserved_OxStress_Genes.txt")]

data = data.loc[data.index.intersection(genes)]

# transpose for PCA
data = data.T

# normalize
X = StandardScaler().fit_transform(data)

# PCA
pca = PCA(n_components=2)
pcs = pca.fit_transform(X)

# labels
labels = ["Control"]*len(ctrl) + ["Stress"]*len(stress)

# -----------------------------
# plot
# -----------------------------
plt.figure(figsize=(6,5))

for lab, color in zip(["Control","Stress"],["blue","red"]):
    idx = [i for i,l in enumerate(labels) if l==lab]
    plt.scatter(pcs[idx,0], pcs[idx,1], label=lab)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Predictive Power of Conserved Oxidative-Stress Core")
plt.legend()
plt.tight_layout()

plt.savefig("figures/Figure14_Predictive_Stress_Score.png", dpi=300)

print("Figure15 created")
