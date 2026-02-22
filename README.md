# Conserved Chromatin-Centred Regulatory Architecture of Oxidative Stress Across Human Cell Types

## Overview

This repository contains the complete computational framework supporting the manuscript:

**“Conserved Chromatin-Centred Regulatory Architecture Defines Oxidative Stress Adaptation Across Human Cell Types.”**

The study identifies a reproducible oxidative stress program across epithelial and endothelial systems using cross-dataset transcriptomic integration, enrichment analysis, transcription factor inference, and protein interaction network topology.

The findings suggest that oxidative stress adaptation is organised around a conserved chromatin-centred regulatory architecture rather than a fixed antioxidant gene signature.

---

## Datasets

All datasets were obtained from the NCBI Gene Expression Omnibus (GEO).

### Discovery
- ARPE-19 epithelial oxidative stress dataset

### Validation
- GSE299876 – ARPE-19 RNA-seq oxidative stress dataset
- GSE208105 – Endothelial (HUVEC) oxidative stress dataset

Only publicly available data were used.

---

## Repository Structure

oxidative-stress-architecture/

- scripts/ → All analysis scripts  
- figures/ → Figures 1–15 used in manuscript  
- tables/ → Tables 1–6  
- data_processed/ → Processed outputs and enrichment results  
- gene_lists/ → Conserved genes and derived lists  
- supplementary/ → Supplementary outputs  

---

## Analysis Pipeline

1. Differential expression analysis (DESeq2 framework)
2. Cross-dataset intersection to identify conserved genes
3. Stringency-dependent robustness testing
4. Gene ontology enrichment (Enrichr via gseapy)
5. Transcription factor enrichment (ChEA, ENCODE, TRRUST)
6. STRING protein–protein interaction mapping
7. Network centrality analysis (NetworkX)
8. Direction-independent program enrichment
9. Predictive oxidative stress scoring

---

## Conserved Oxidative Stress Gene Core

BRD4  
EIF4G1  
GANAB  
ITGA3  
LMNA  
MBOAT7  
NSD2  
PTPRF  
SLC2A1  
SMARCA4  
STAT2  
WDR1  

These genes are enriched for chromatin regulation, transcriptional coordination, membrane organisation, and metabolic adaptation.

---

## Key Findings

- Gene-level overlap across models is limited.
- Functional convergence is conserved across tissues.
- Chromatin regulators (BRD4, SMARCA4, NSD2) function as central network hubs.
- Direction-independent enrichment supports regulatory state transition.
- The 12-gene core alone separates control vs stress samples (p ≈ 1 × 10⁻¹⁶).
- A conserved oxidative stress score demonstrates predictive discrimination.

---

## Reproducibility

All scripts required to reproduce figures and tables are located in:

scripts/

Processed intermediate outputs are provided in:

data_processed/

The analysis is modular and reproducible.

---

## Software Requirements

- Python 3.10+
- R (DESeq2)
- pandas
- numpy
- matplotlib
- networkx
- gseapy

---

## Data Availability

Raw data are publicly available through GEO:
- GSE299876
- GSE208105

Processed outputs used in figure generation are included in this repository.

---

## Author

Mohd Mehboob Uddin  
Independent Computational Redox Biology Research

---

## License

This repository is provided for academic and research use.
