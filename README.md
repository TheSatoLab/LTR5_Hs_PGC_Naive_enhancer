# LTR5\_Hs\_PGC\_Naive\_enhancer

This is a repository of the programs used in the paper [Ito et al., bioRxiv, 2021].
The related data are available via the Mendeley data repository (http://dx.doi.org/10.17632/w5gfs9mdrr.1).

Although the gene regulatory networks of germ cells are critical for gamete integrity, these networks have been diversified during mammalian evolution. Here, we show that numerous copies of LTR5\_Hs, a hominoid-specific endogenous retrovirus (ERV), function as enhancers in both human primordial germ cells (PGCs) and naïve pluripotent cells. Multiomics analysis suggested that PGCs and naïve pluripotent cells exhibit a similar transcriptome signature, and enhancers derived from LTR5\_Hs contribute to establishing such similarity. LTR5\_Hs appears to be activated by transcription factors critical in both cell types (KLF4, TFAP2C, NANOG, and CBFA2T2). Comparative transcriptome analysis between humans and macaques suggested that the expression of many genes in PGCs and naïve pluripotent cells has been upregulated by LTR5\_Hs insertions in the hominoid lineage. Together, the present study demonstrates that LTR5\_Hs insertions may have rewired and finetuned the gene regulatory network shared between PGCs and naïve pluripotent cells during hominoid evolution.

## Contents:
* **PGC\_specific\_expression\_score:** for calculattion the PGC-specific expression score for each genes. The PGC-specific expression score represents how the expression pattern is similar to the modeled “PGCLC-specific” expression pattern.
* **remove\_redundant\_gene\_sets:**  for removing the redundant gene sets whose members highly overlapped with each other from the result of Gene Ontology enrichment analysis.
* **GREAT\_pairwise:**  for performing the GREAT enrichment analysis (https://www.nature.com/articles/nbt.1630) with the user-defined background regions.
* **genome\_permutation\_test:**  for calculating the enrichment of overlaps between the two sets of features according to genomic permutation test.

