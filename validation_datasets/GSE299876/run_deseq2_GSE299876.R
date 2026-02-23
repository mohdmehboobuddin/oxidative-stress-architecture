library(DESeq2)

# Load count matrix
counts <- read.csv("GSE299876_ARPE_count_matrix.csv", row.names=1)

# Define sample groups
condition <- factor(c("Control","Control","Control",
                      "H2O2","H2O2","H2O2"))

coldata <- data.frame(row.names=colnames(counts),
                      condition)

# Create DESeq2 dataset
dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData = coldata,
                              design = ~ condition)

# Filter low counts
dds <- dds[rowSums(counts(dds)) > 10, ]

# Run DESeq2
dds <- DESeq(dds)

res <- results(dds)

# Order by p-value
resOrdered <- res[order(res$pvalue), ]

# Save results
write.csv(as.data.frame(resOrdered),
          file="GSE299876_ARPE_DESeq2_results.csv")

cat("DESeq2 completed successfully.\n")
