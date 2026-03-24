import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

# load
ctrl = pd.read_csv("GSM6337370_HUVEC_LVCON.Gene.rpkm.txt", sep="\t")
stress = pd.read_csv("GSM6337371_HUVEC_LVCON_H2O2.Gene.rpkm.txt", sep="\t")

ctrl = ctrl[['Symbol','RPKM']]
stress = stress[['Symbol','RPKM']]

ctrl.columns=['gene','ctrl']
stress.columns=['gene','stress']

df = pd.merge(ctrl,stress,on='gene')

df['log2FC']=np.log2((df['stress']+1)/(df['ctrl']+1))

# load conserved genes
with open("../../Figure6_Conserved_OxStress_Genes.txt") as f:
    conserved=set([x.strip() for x in f if x.strip()])

cons=df[df['gene'].isin(conserved)]['log2FC']
bg=df[~df['gene'].isin(conserved)]['log2FC']

stat,p=mannwhitneyu(cons,bg,alternative='greater')

print("Median conserved:",np.median(cons))
print("Median background:",np.median(bg))
print("Enrichment p-value:",p)
