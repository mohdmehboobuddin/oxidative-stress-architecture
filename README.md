cat > README.md << 'EOF'
Conserved Chromatin-Centred Regulatory Architecture of Oxidative Stress Adaptation

Overview

This repository contains the complete computational framework supporting the manuscript:

**“Conserved Chromatin-Centred Regulatory Architecture Defines Oxidative Stress Adaptation Across Cellular Systems.”**

The study identifies a reproducible oxidative stress program across epithelial and endothelial systems.

The findings support a model in which oxidative stress adaptation is organised around a conserved chromatin-centred regulatory architecture.

---

Datasets

All datasets were obtained from the NCBI Gene Expression Omnibus (GEO).

Discovery Dataset

ARPE-19 epithelial oxidative stress dataset

Validation Datasets

GSE299876 – ARPE-19 RNA-seq oxidative stress dataset
GSE208105 – Endothelial (HUVEC) oxidative stress dataset

Only publicly available data were used.

---

Repository Structure

oxidative-stress-architecture/

├── scripts/               # Analysis scripts
├── figures/               # Figures 1–15
├── tables/                # Tables 1–6
├── data_processed/        # Processed outputs and enrichment results
├── gene_lists/            # Conserved gene sets
├── supplementary/         # Supplementary figures and tables
├── requirements.txt
└── README.md

---

Computational Workflow

The analysis pipeline includes:

1. Differential expression analysis (DESeq2 framework)
2. Cross-dataset intersection for conserved gene identification
3. Stringency-dependent robustness testing
4. Gene Ontology enrichment (Enrichr via gseapy)
5. Transcription factor enrichment (ChEA, ENCODE, TRRUST)
6. STRING protein–protein interaction mapping
7. Network centrality analysis (NetworkX)
8. Direction-independent program enrichment
9. Predictive oxidative stress scoring

---

Conserved Oxidative Stress Gene Core

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

These genes are enriched for chromatin regulation, transcriptional coordination and metabolic adaptation.

---

Key Findings

Gene-level overlap across models is limited.
Functional convergence is conserved across tissues.
Chromatin regulators (BRD4, SMARCA4, NSD2) function as central network hubs.
Direction-independent enrichment supports regulatory state transition.
The 12-gene core alone separates control vs stress samples (p ≈ 1 × 10⁻¹⁶).
A conserved oxidative stress score demonstrates predictive discrimination.

---

Reproduction Guide

Example commands:

python scripts/validation_overlap_GSE299876.py
python scripts/analyze_network_centrality.py
python scripts/figure14_direction_independent_program.py
python scripts/figure15_predictive_power.py

---

Software Requirements

Python 3.10+
R (DESeq2)
pandas
numpy
matplotlib
networkx
gseapy
scipy
seaborn

Install dependencies:

pip install -r requirements.txt

---

Supplementary Material

All supplementary figures and tables associated with the manuscript are available in the `supplementary/` directory of this repository.

This includes:
Supplementary Figures S1–S4
Supplementary Tables S1–S3

These files correspond directly to the supplementary material submitted alongside the manuscript and support reproducibility of robustness, enrichment and network analyses.

---

Data Availability

Raw data are publicly available via GEO:

GSE299876
GSE208105

Processed outputs used for figure generation are included in this repository.

---

Author

Mohd Mehboob Uddin
Independent computational systems biology research project.

---

License

This repository is provided for academic and research use.
EOF
