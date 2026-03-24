# DESeq2 Differential Expression Analysis

library(DESeq2)

# Load count data
counts <- read.csv("data_processed/count_matrix.csv", row.names = 1)
metadata <- read.csv("data_processed/metadata.csv", row.names = 1)

# Create DESeq2 object
dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData = metadata,
                              design = ~ condition)

# Run DESeq2
dds <- DESeq(dds)

# Extract results
res <- results(dds)

# Save results
write.csv(as.data.frame(res), file = "data_processed/deseq2_results.csv")
