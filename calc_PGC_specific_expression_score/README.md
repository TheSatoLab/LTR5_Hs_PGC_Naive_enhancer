# calc_PGC_specific_expression_score

For calculattion the PGC-specific expression score for each genes. The PGC-specific expression score represents how the expression pattern is similar to the modeled “PGCLC-specific” expression pattern.

## Contents:
* **calc\_PGC\_specific\_expression\_score.R:** a R script
* **cell\_info.txt:** cell type information
* **gene\_TE\_type.txt:** gene/TE-type information
* **data.merged.vitro.count.subfamily.logNorm.head\_2000.csv:** an expression matrix including relative expression values [log2(Counts per Million + 1)]

## Usage:
~~~
R --vanilla --slave --args \
  cell_info.txt \
  gene_TE_type.txt \
  data.merged.vitro.count.subfamily.logNorm.head_2000.csv \
  res_PGC_specific_expression_score.txt \
  < calc_PGC_specific_expression_score.R
~~~

## Dependencies:
* R (version 3.6.3)
	* tidyverse

