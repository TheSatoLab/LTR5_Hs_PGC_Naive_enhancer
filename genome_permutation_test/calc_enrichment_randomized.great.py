#!/usr/bin/env python

import sys, math, subprocess, re
import numpy as np
import scipy.stats as stats

argvs = sys.argv


bed1_f_name = argvs[1]
genome_f_name = argvs[2]
num_permutation = 100

def countOnTFBS(F2_name,F1_name):
  Cmd = 'bedtools \
          intersect -sorted -a \"%(f1_name)s\" -b \"%(f2_name)s\" -wa | sort | uniq | wc -l | cut -f 1' %{"f1_name":F1_name,"f2_name":F2_name} 
  Count = int(subprocess.check_output(Cmd, shell=True).strip())
  return Count

def generateRandomCountList(F2_name,F1_name,Genome_f_name):
  Count_random_l = []  
  for i in range(1, num_permutation + 1):
    Cmd = 'bedtools \
           shuffle -noOverlapping -i \"%(f1_name)s\" -g \"%(genome_f_name)s\" | \
           sort -k 1,1 -k 2,2n | \
           bedtools \
           intersect -sorted -a \"stdin\" -b \"%(f2_name)s\" -wa | \
           sort | uniq | wc -l | cut -f 1' %{"f1_name":F1_name,"f2_name":F2_name, "genome_f_name":Genome_f_name} 
    Count_random = int(subprocess.check_output(Cmd, shell=True).strip())
    Count_random_l.append(Count_random)
  return Count_random_l

def calcPvalUponPoissondist(Count,Mean):
  from scipy.stats import poisson
  if Count >= Mean:
    Pval = poisson.sf(Count,Mean)*2
  else:
    Pval = poisson.cdf(Count,Mean)*2
  return Pval





print "gs_name\tcount\tfold_enrichment\tz_score\tpval_Norm\tpval_Poisson"
for bed2_f_name in argvs[3:]:
  gs_name = re.sub(r'([^\/]+)\.bed',r'\1',bed2_f_name)
  count_observed = countOnTFBS(bed1_f_name,bed2_f_name)

  count_random_l = generateRandomCountList(bed1_f_name,bed2_f_name,genome_f_name)
  mean_count_random = np.mean(count_random_l)
  sd_count_random = np.std(count_random_l)

  fe = count_observed / mean_count_random
  z_score = (count_observed - mean_count_random) / sd_count_random
  pval_Norm = stats.norm.sf(abs(z_score))*2
  pval_Poisson = calcPvalUponPoissondist(count_observed,mean_count_random)
  res_l = [gs_name,count_observed,fe,z_score,pval_Norm,pval_Poisson]
  print "\t".join([str(c) for c in res_l])

