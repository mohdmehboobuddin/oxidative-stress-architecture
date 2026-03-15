# Conserved Chromatin-Centred Regulatory Architecture Underlies Oxidative Stress Adaptation

This repository contains the complete computational workflow supporting the manuscript:

**“A Conserved Chromatin-Centred Regulatory Architecture Underlies Oxidative Stress Adaptation Across Cellular Systems.”**

The project integrates transcriptomic datasets from epithelial and endothelial systems to identify a conserved regulatory scaffold governing oxidative stress adaptation.

---

## Project Overview

Oxidative stress is traditionally defined as an imbalance between reactive oxygen species (ROS) and antioxidant defences. However, transcriptomic studies of oxidative stress frequently produce highly heterogeneous gene-level results across biological systems.

This project applies a **systems-level transcriptomic framework** to identify conserved regulatory architecture underlying oxidative stress adaptation.

The computational pipeline integrates:

• Cross-model transcriptomic integration  
• Stringency-dependent conservation analysis  
• Gene ontology and pathway enrichment  
• Transcription factor regulatory inference  
• Protein-protein interaction network topology  
• Network centrality analysis  
• Direction-independent functional enrichment  
• Predictive PCA-based stress scoring  

These analyses reveal a **compact chromatin-centred regulatory architecture** driving oxidative stress adaptation across cellular systems.

---

## Conserved Oxidative Stress Gene Core

A reproducible **12-gene conserved program** was identified across independent oxidative stress datasets:

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

Functional roles of the conserved architecture:

Chromatin regulation: BRD4, SMARCA4, NSD2  
Signal integration: STAT2, PTPRF  
Metabolic adaptation: SLC2A1, MBOAT7, GANAB  
Structural / nuclear integrity: ITGA3, LMNA, WDR1, EIF4G1  

Network centrality analysis identifies **BRD4 and SMARCA4 as dominant regulatory hubs**.

Principal component analysis using only the 12-gene core robustly separates oxidative stress and control states (**p ≈ 1 × 10⁻¹⁶**).

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
├── data_processed/              # Processed analysis outputs
├── gene_lists/                  # Conserved gene sets
│
├── requirements.txt             # Python dependency list
└── README.md
```

All figures and tables in the **results/** directory correspond exactly to the numbering used in the manuscript.

---

## Computational Workflow

The computational pipeline consists of the following steps:

1. Differential expression analysis (DESeq2)
2. Cross-dataset conservation intersection
3. Stringency-dependent robustness testing
4. Gene ontology enrichment analysis (Enrichr / gseapy)
5. Transcription factor enrichment analysis (ChEA / ENCODE)
6. Protein-protein interaction mapping (STRING)
7. Network topology analysis (NetworkX centrality metrics)
8. Direction-independent enrichment analysis
9. Predictive oxidative stress scoring

---

## Data Sources

All datasets were obtained from the **NCBI Gene Expression Omnibus (GEO)**.

GSE122270 — ARPE-19 oxidative stress microarray  
GSE158909 — iPSC-derived RPE RNA-seq dataset  
GSE299876 — ARPE-19 RNA-seq validation dataset  
GSE208105 — HUVEC endothelial oxidative stress dataset  

Large raw sequencing files are hosted on GEO and are **not duplicated in this repository**.

---

## Reproducing the Analysis

Install required packages:

```
pip install -r requirements.txt
```

Example analysis commands:

```
python scripts/validation_overlap_GSE299876.py
python scripts/analyze_network_centrality.py
python scripts/figure_direction_independent_program.py
python scripts/figure_predictive_power.py
```

Processed outputs used to generate manuscript figures are available in the **results/** directory.

---

## Manuscript Outputs

Main manuscript:

Tables  
Table 1 — Dataset overview  
Table 2 — Conserved oxidative stress gene list  

Figures  
Figure 1 — Gene ontology enrichment analysis  
Figure 2 — Endothelial validation of conserved program  
Figure 3 — Direction-independent functional enrichment  
Figure 4 — PCA using conserved gene core  
Figure 5 — STRING protein interaction network  
Figure 6 — Integrated regulatory architecture model  

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

## License

This repository is provided for academic and research use.
