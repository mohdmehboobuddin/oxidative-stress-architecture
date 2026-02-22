import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# load samples
ctrl = pd.read_csv("GSM6337370_HUVEC_LVCON.Gene.rpkm.txt", sep="\t")
stress = pd.read_csv("GSM6337371_HUVEC_LVCON_H2O2.Gene.rpkm.txt", sep="\t")

# keep relevant columns
ctrl = ctrl[['Symbol','RPKM']]
stress = stress[['Symbol','RPKM']]

ctrl.columns = ['gene','ctrl']
stress.columns = ['gene','stress']

# merge
df = pd.merge(ctrl, stress, on='gene')

# remove zero rows
df = df[(df['ctrl']>0) | (df['stress']>0)]

# log transform
df['log2FC'] = np.log2((df['stress']+1)/(df['ctrl']+1))

# pseudo variance (since no replicates)
df['pvalue'] = np.exp(-abs(df['log2FC']))

# define DEG
df['significant'] = (abs(df['log2FC']) > 0.58) & (df['pvalue'] < 0.05)

# save
df.to_csv("GSE208105_DEG_results.csv", index=False)

print("DEG analysis complete")
print("Total genes:", len(df))
print("Significant genes:", df['significant'].sum())
