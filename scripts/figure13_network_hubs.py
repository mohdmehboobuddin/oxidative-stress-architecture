import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Network_Centrality.csv")
df=df.sort_values("eigenvector",ascending=True)

plt.figure(figsize=(6,5))
plt.barh(df["gene"],df["eigenvector"])
plt.xlabel("Eigenvector Centrality")
plt.title("Hub Regulators of Conserved Oxidative Stress Architecture")
plt.tight_layout()
plt.savefig("figures/Figure13_Network_Hub_Centrality.png", dpi=300)
print("Hub figure created")
