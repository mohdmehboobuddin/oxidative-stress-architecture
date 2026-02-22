import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# load STRING network
df = pd.read_csv("string_network.tsv", sep="\t", header=None)

# columns: protein1 protein2 combined_score
df = df[[2,3,5]]
df.columns=["A","B","score"]

# build graph
G = nx.Graph()

for _,row in df.iterrows():
    G.add_edge(row["A"], row["B"], weight=row["score"])

# centrality measures
degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
eigen = nx.eigenvector_centrality(G, max_iter=1000)

centrality = pd.DataFrame({
    "gene": list(degree.keys()),
    "degree": list(degree.values()),
    "betweenness": [betweenness[g] for g in degree.keys()],
    "eigenvector": [eigen[g] for g in degree.keys()]
})

centrality.sort_values("eigenvector", ascending=False, inplace=True)
centrality.to_csv("Network_Centrality.csv", index=False)

print(centrality)
