# Conserved Chromatin-Centered Regulatory Architecture Underlies Oxidative Stress Adaptation

This repository contains the complete computational workflow used to integrate cross-model transcriptomic data and identify a conserved regulatory scaffold for oxidative stress adaptation.

## Project Overview

Oxidative stress is traditionally defined as a biochemical imbalance between reactive oxygen species and antioxidant defenses. However, transcriptomic studies often produce highly heterogeneous gene-level results, making it difficult to identify consistent regulatory mechanisms.

This study implements a systems-level computational framework to identify conserved transcriptional architecture across independent datasets.

The analytical strategy integrates:
- Cross-model transcriptomic harmonization (epithelial and endothelial systems)
- Stringency-dependent conserved gene identification
- Direction-independent functional enrichment (Gene Ontology and Reactome)
- Protein–protein interaction network analysis (centrality mapping)
- Principal component-based predictive modeling of stress states

Rather than focusing on classical antioxidant genes, this work identifies a compact regulatory core driven by chromatin-associated factors.

## Repository Structure

oxidative-stress-architecture/
├── data/
├── data_processed/
├── results/
│   ├── main_figures/
│   ├── main_tables/
│   ├── supplementary_figures/
│   └── supplementary_tables/
├── scripts/
├── gene_lists/
├── requirements.txt
└── README.md

All figures and tables in the `results/` directory directly correspond to those presented in the manuscript.

## Conserved Oxidative Stress Gene Core

BRD4, EIF4G1, GANAB, ITGA3, LMNA, MBOAT7, NSD2, PTPRF, SLC2A1, SMARCA4, STAT2, WDR1

Functional organization:
- Chromatin and epigenetic regulation: BRD4, SMARCA4, NSD2
- Signal integration: STAT2, PTPRF
- Metabolic adaptation: SLC2A1, MBOAT7, GANAB
- Structural and nuclear integrity: ITGA3, LMNA, WDR1, EIF4G1

Key finding:
This 12-gene core alone separates oxidative stress and control samples with strong statistical significance (p ≈ 1 × 10⁻¹⁶), independent of fold-change direction.

## Data Sources

All datasets are publicly available from the NCBI Gene Expression Omnibus (GEO):
- GSE122270 — ARPE-19 microarray
- GSE158909 — iPSC-derived RPE RNA-seq
- GSE299876 — ARPE-19 RNA-seq
- GSE208105 — HUVEC endothelial RNA-seq

To reproduce the analysis:
Download the required count matrices from GEO and place them in:

data_raw/

Raw sequencing files are not included due to size constraints.

## Reproducing the Analysis

This pipeline was developed and tested using:
- Python 3.9+
- R (DESeq2)

### Important note:
Differential expression analysis was performed using DESeq2 in R.  
All downstream analyses (network analysis, enrichment, and figure generation) were performed in Python.

### Execution workflow:

Step 1 — Differential expression (R):
scripts/01_deseq2_analysis.R

Step 2 — Generate processed data:
Outputs will be stored in data_processed/

Step 3 — Generate figures and analyses (Python):
python scripts/figure2_validation.py  
python scripts/figure3_direction_independent.py  
python scripts/figure4_pca_core.py  
python scripts/figure5_network_analysis.py  
python scripts/figure6_model.py  

All scripts are designed to run independently once processed data is available.

## Software Requirements

Python libraries:
pandas  
numpy  
matplotlib  
networkx  
gseapy  
scipy  

R packages:
DESeq2  

Install Python dependencies:
pip install -r requirements.txt

## Key Findings

- Gene-level overlap across datasets is limited  
- Functional convergence is conserved across systems  
- Chromatin regulators act as dominant network hubs  
- Oxidative stress responses are direction-independent  
- A minimal gene set predicts stress state with high accuracy  
- The response reflects a regulatory state transition rather than simple activation  

These findings support a model in which oxidative stress represents a coordinated transcriptional reorganization rather than a purely antioxidant-driven response.

## Authors

Mohd Mehboob Uddin  
Syed Mohd Zakariya Ali Khan  
Sridhar Gunde  

Department of Life Sciences  
A.V. College of Arts, Science and Commerce  
Osmania University, Hyderabad, India  

## Citation

If you use this code or functional gene list in your research, please cite:

Uddin, M.M., Khan, S.M.Z.A., & Gunde, S. (2026). A Conserved Chromatin-Centered Regulatory Architecture Underlies Oxidative Stress Adaptation Across Cellular Systems. Frontiers in Genetics (under review). DOI: to be assigned.

## License

This repository is provided for academic and research use.
