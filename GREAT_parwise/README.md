# GREAT_pairwise
For performing the GREAT enrichment analysis (https://www.nature.com/articles/nbt.1630) with the user-defined background regions.

## Contents:
* **great_pairwise.py:** a python2.7 script
* **integrated_ATAC.naive_PGCLC.both_up_peak.bed:** a bed file for features of interest 
* **tss.bs.50kb.bed:** a bed file for the transcription start sites (TSSs) of all protein-coding genes
* **bed/*.bed:** bed file(s) for the TSSs of the set(s) of genes of interest

## Usage:
~~~
python2 great_pairwise.py \
  integrated_ATAC.naive_PGCLC.both_up_peak.bed \
  tss.bs.50kb.bed \
  bed/*.bed \
  > res_great_naive_PGCLC.both_up_peak.txt
~~~

## Dependencies:
* Python2.7
	* sys, math, subprocess, re, scipy
* bedtoools (v2.27.0)
