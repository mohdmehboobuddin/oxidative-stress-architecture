import re
import matplotlib.pyplot as plt

tfs=[]
scores=[]

with open("TF_enrichment_ChEA_2022.txt") as f:
    for line in f.readlines()[:10]:
        name=line.split("'")[1].split()[0]
        p=float(line.split(",")[2])
        tfs.append(name)
        scores.append(-__import__("math").log10(p))

plt.figure(figsize=(6,4))
plt.barh(tfs,scores)
plt.xlabel("-log10(p-value)")
plt.title("Key Regulators of Conserved Oxidative Stress Architecture")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("figures/Figure9_Chromatin_Control_Modules.png", dpi=300)

print("TF figure created")
