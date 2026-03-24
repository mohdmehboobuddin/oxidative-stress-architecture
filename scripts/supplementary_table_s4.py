import pandas as pd

# -----------------------------
# Load GO enrichment results
# -----------------------------
go = pd.read_csv("Figure7A_GO_Function_ALL.csv")

# Safety check
required_cols = ["Term", "Adjusted P-value", "Genes"]
for col in required_cols:
    if col not in go.columns:
        raise ValueError(f"Missing column: {col}")

# -----------------------------
# Clean and prepare
# -----------------------------
go = go.dropna(subset=["Adjusted P-value", "Genes"])
go = go.sort_values("Adjusted P-value")

# Keep only biologically meaningful top terms
top_terms = go.head(12).copy()

# Split gene list and count
top_terms["Gene_Count"] = top_terms["Genes"].apply(
    lambda x: len(str(x).split(";"))
)

# Add readable descriptions
top_terms["Description"] = top_terms["Term"].apply(
    lambda x: x.replace("_", " ").replace("GO:", "")
)

# Manual functional categorization (important for reviewers)
def categorize(term):
    term = term.lower()
    if "stress" in term or "response" in term:
        return "Oxidative Stress Response"
    if "chromatin" in term or "transcription" in term:
        return "Chromatin / Transcriptional Control"
    if "metabolic" in term or "glucose" in term:
        return "Metabolic Regulation"
    if "immune" in term or "interferon" in term:
        return "Immune / Inflammatory Signaling"
    return "Cellular Homeostasis"

top_terms["Category"] = top_terms["Description"].apply(categorize)

# -----------------------------
# Final Table 4
# -----------------------------
table4 = top_terms[
    [
        "Term",
        "Description",
        "Gene_Count",
        "Genes",
        "Adjusted P-value",
        "Category"
    ]
].rename(columns={
    "Adjusted P-value": "Adjusted_P_Value"
})

# Save
table4.to_csv("Table4_Functional_Convergence_of_Conserved_Genes.csv", index=False)

print("✅ Table 4 generated successfully")
print(table4)
