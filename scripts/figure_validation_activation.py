import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load expression
ctrl = pd.read_csv("validation_datasets/GSE208105/GSM6337370_HUVEC_LVCON.Gene.rpkm.txt", sep="\t")
stress = pd.read_csv("validation_datasets/GSE208105/GSM6337371_HUVEC_LVCON_H2O2.Gene.rpkm.txt", sep="\t")

ctrl = ctrl[['Symbol','RPKM']]
stress = stress[['Symbol','RPKM']]

ctrl.columns=['gene','ctrl']
stress.columns=['gene','stress']

df = pd.merge(ctrl,stress,on='gene')
df['log2FC']=np.log2((df['stress']+1)/(df['ctrl']+1))

# conserved genes
with open("Figure6_Conserved_OxStress_Genes.txt") as f:
    conserved=set([x.strip() for x in f if x.strip()])

df['group'] = df['gene'].apply(lambda x: 'Conserved' if x in conserved else 'Background')

# plot
plt.figure(figsize=(6,5))

bg = df[df['group']=="Background"]['log2FC']
cons = df[df['group']=="Conserved"]['log2FC']

plt.boxplot([bg,cons], labels=['Genome','Conserved'])
plt.axhline(0, linestyle='--')

plt.ylabel("log2 Fold Change (H2O2 vs Control)")
plt.title("Activation of Conserved Oxidative Stress Architecture in Endothelial Cells")

plt.tight_layout()
plt.savefig("Figure9_Architecture_Activation_Validation.png", dpi=300)
print("Figure created")
