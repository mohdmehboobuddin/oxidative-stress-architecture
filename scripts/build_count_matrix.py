import pandas as pd
import glob

# Select only ARPE samples
files = [
    "GSM9048232_ARPE_Ctrl_rep1.txt",
    "GSM9048233_ARPE_Ctrl_rep2.txt",
    "GSM9048234_ARPE_Ctrl_rep3.txt",
    "GSM9048235_ARPE_H2O2_rep1.txt",
    "GSM9048236_ARPE_H2O2_rep2.txt",
    "GSM9048237_ARPE_H2O2_rep3.txt",
]

dfs = []

for f in files:
    sample_name = f.replace(".txt", "")
    df = pd.read_csv(f, sep="\t", header=None)
    df.columns = ["Gene", sample_name]
    dfs.append(df)

# Merge all on Gene column
from functools import reduce
merged = reduce(lambda left, right: pd.merge(left, right, on="Gene"), dfs)

merged.to_csv("GSE299876_ARPE_count_matrix.csv", index=False)

print("Count matrix created successfully.")
