# genome_permutation_test
For calculating the enrichment of overlaps between the two sets of features according to genomic permutation test.

## Contents:
* **calc\_enrichment\_randomized.great.py:** a python2.7 script
* **Q92754__TFAP2C.bed:** a bed file for feature1. The genome positions of the feature1 are shuffled.
* **chromSize\_hg38.txt:** a file describing chromosome length
* **LTR5\_Hs.with_signal.bed:** a bed file for feature1.

## Usage:
~~~
python2 calc_enrichment_randomized.great.py \
        Q92754__TFAP2C.bed \
        chromSize_hg38.txt \
        LTR5_Hs.with_signal.bed \
        > res_enrichment_TFAP2C_on_LTR5_Hs.txt
~~~

## Dependencies:
* Python2.7
	* sys, math, subprocess, re, numpy, scipy
* bedtools (v2.27.0)
