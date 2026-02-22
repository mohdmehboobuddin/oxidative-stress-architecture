import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load STRING file WITHOUT header
df = pd.read_csv("data_processed/string_network.tsv", sep="\t", header=None)

# STRING format (standard export):
# Column 0 = protein1 (ENSP)
# Column 1 = protein2 (ENSP)
# Column 2 = gene name A
# Column 3 = gene name B
# Last column = combined score

proteinA_col = 2
proteinB_col = 3
score_col = df.shape[1] - 1

G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row[proteinA_col],
               row[proteinB_col],
               weight=row[score_col])

# Compute centrality
degree = nx.degree_centrality(G)

node_sizes = [degree[n] * 4000 for n in G.nodes()]

pos = nx.spring_layout(G, seed=42, k=0.6)

plt.figure(figsize=(12,8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("STRING Protein–Protein Interaction Network\nConserved Oxidative Stress Gene Core", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.savefig("figures/Figure12_STRING_Network.png", dpi=600)
plt.close()
