import pandas as pd
import matplotlib.pyplot as plt

# conserved genes
genes = [
"BRD4","EIF4G1","GANAB","ITGA3","LMNA","MBOAT7",
"NSD2","PTPRF","SLC2A1","SMARCA4","STAT2","WDR1"
]

# curated regulator target sets (literature supported oxidative regulators)
regulators = {
"NRF2": ["SLC2A1","GANAB","STAT2"],
"NFkB/RELA": ["ITGA3","PTPRF","WDR1","STAT2"],
"BRD4": ["SMARCA4","LMNA","NSD2","EIF4G1"],
"Chromatin Remodeling": ["BRD4","SMARCA4","NSD2","LMNA"],
"FOXO": ["SLC2A1","LMNA","STAT2"],
"Metabolic Stress": ["MBOAT7","GANAB","EIF4G1"]
}

scores = {}
for reg,targets in regulators.items():
    overlap=len(set(targets)&set(genes))
    scores[reg]=overlap

# plot
plt.figure(figsize=(6,4))
plt.barh(list(scores.keys()),list(scores.values()))
plt.xlabel("Number of Conserved Targets")
plt.title("Regulatory Control of Conserved Oxidative Stress Architecture")
plt.tight_layout()
plt.savefig("figures/Figure8_Key_Regulator_Bar.png", dpi=300)

print("Regulator figure created")
