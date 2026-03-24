# Conserved Chromatin-Centered Regulatory Architecture Underlies Oxidative Stress Adaptation

This repository contains the complete computational workflow supporting the manuscript:

**“A Conserved Chromatin-Centered Regulatory Architecture Underlies Oxidative Stress Adaptation Across Cellular Systems.”**

The study integrates transcriptomic datasets across epithelial and endothelial systems to identify a conserved regulatory framework underlying oxidative stress adaptation.

---

## Project Overview

Oxidative stress is traditionally defined as an imbalance between reactive oxygen species (ROS) and antioxidant defenses. However, transcriptomic studies of oxidative stress often exhibit substantial gene-level heterogeneity across experimental systems.

This study applies a systems biology framework to identify conserved regulatory architecture underlying oxidative stress responses.

The computational pipeline integrates:

• Cross-model transcriptomic integration  
• Stringency-dependent conservation analysis  
• Gene ontology and pathway enrichment  
• Transcription factor regulatory inference  
• Protein–protein interaction network topology  
• Network centrality analysis  
• Direction-independent functional enrichment  
• Principal component-based predictive modeling  

These analyses reveal a conserved chromatin-centered regulatory architecture underlying oxidative stress adaptation.

---

## Conserved Oxidative Stress Gene Core

A reproducible 12-gene conserved program was identified across independent datasets:

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

Functional categorization:

Chromatin regulation: BRD4, SMARCA4, NSD2  
Signal integration: STAT2, PTPRF  
Metabolic adaptation: SLC2A1, MBOAT7, GANAB  
Structural and nuclear integrity: ITGA3, LMNA, WDR1, EIF4G1  

Network analysis identifies BRD4 and SMARCA4 as dominant regulatory hubs.  
Principal component analysis using the conserved core robustly separates oxidative stress and control states (p ≈ 1 × 10⁻¹⁶).

---

## Repository Structure

```
oxidative-stress-architecture/

├── scripts/                     # Analysis scripts
│
├── results/
│   ├── main_figures/            # Figures 1–6 (main manuscript)
│   ├── main_tables/             # Tables 1–2 (main manuscript)
│   ├── supplementary_figures/   # Supplementary Figures S1–S8
│   └── supplementary_tables/    # Supplementary Tables S1–S7
│
├── data_processed/              # Processed outputs
├── gene_lists/                  # Conserved gene sets
│
├── requirements.txt             # Python dependencies
└── README.md
```

All files in the `results/` directory correspond exactly to the numbering used in the manuscript.

---

## Computational Workflow

The analysis pipeline consists of the following steps:

1. Differential expression analysis using DESeq2  
2. Cross-dataset conservation intersection  
3. Stringency-dependent robustness analysis  
4. Gene ontology enrichment (Enrichr via gseapy)  
5. Transcription factor enrichment (ChEA / ENCODE)  
6. Protein–protein interaction mapping (STRING)  
7. Network topology analysis (NetworkX)  
8. Direction-independent enrichment analysis  
9. Predictive oxidative stress scoring  

**Note:** Differential expression analysis was performed using the DESeq2 statistical framework (R-based), and downstream analyses were performed in Python.

---

## Data Sources

All datasets were obtained from the NCBI Gene Expression Omnibus (GEO):

GSE122270 — ARPE-19 oxidative stress microarray  
GSE158909 — iPSC-derived RPE RNA-seq dataset  
GSE299876 — ARPE-19 RNA-seq validation dataset  
GSE208105 — HUVEC endothelial oxidative stress dataset  

Raw sequencing data are hosted on GEO and are not included in this repository.

To reproduce the analysis:

Download the required count matrices from GEO and place them in a directory named:

```
data_raw/
```

before running the analysis scripts.

---

## Reproducing the Analysis

This pipeline was developed and tested using **Python 3.9+**.

Install dependencies:

```
pip install -r requirements.txt
```

### Execution order

1. Perform differential expression analysis (DESeq2, R)
2. Generate processed outputs (stored in `data_processed/`)
3. Run figure scripts to reproduce results

Example commands:

```
python scripts/figure1_go_enrichment.py
python scripts/figure2_endothelial_validation.py
python scripts/figure3_direction_independent.py
python scripts/figure4_pca_core.py
```

---

## Reproducibility Guide

Each manuscript figure corresponds to a specific script:

Main Figures:

Figure 1 — scripts/figure1_go_enrichment.py  
Figure 2 — scripts/figure2_endothelial_validation.py  
Figure 3 — scripts/figure3_direction_independent.py  
Figure 4 — scripts/figure4_pca_core.py  
Figure 5 — scripts/figure5_string_network.py  
Figure 6 — scripts/figure6_model.py  

Supplementary Figures:

Figure S1 — scripts/figureS1_volcano.py  
Figure S2 — scripts/figureS2_global_pca.py  
Figure S3 — scripts/figureS3_stringency.py  
Figure S4 — scripts/figureS4_concordance.py  
Figure S5 — scripts/figureS5_relaxed_enrichment.py  
Figure S6 — scripts/figureS6_predictive_score.py  
Figure S7 — scripts/figureS7_tf_enrichment.py  
Figure S8 — scripts/figureS8_networks.py  

---

## Manuscript Outputs

Main manuscript:

Tables  
Table 1 — Dataset overview  
Table 2 — Conserved oxidative stress gene list  

Figures  
Figure 1 — Gene ontology enrichment analysis  
Figure 2 — Endothelial validation  
Figure 3 — Direction-independent enrichment  
Figure 4 — PCA using conserved gene core  
Figure 5 — STRING interaction network  
Figure 6 — Integrated regulatory model  

Supplementary material:

Tables S1–S7  
Figures S1–S8  

---

## Author

Mohd Mehboob Uddin  
Department of Life Sciences  
A.V. College of Arts, Science and Commerce  
Osmania University  
Hyderabad, Telangana, India  

---

## Citation

If you use this code or functional gene list in your research, please cite:

Uddin, M.M. (2026).  
*A Conserved Chromatin-Centered Regulatory Architecture Underlies Oxidative Stress Adaptation Across Cellular Systems.*  
[Journal Name to be updated upon publication]  

---

## License

This repository is provided for academic and research use.
