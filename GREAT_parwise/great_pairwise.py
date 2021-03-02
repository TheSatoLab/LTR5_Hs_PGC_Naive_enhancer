#!/usr/bin/env python

import sys, math, subprocess, re
import scipy.stats as stats
argvs = sys.argv

def countHitonRegdom(F1_name,F2_name):
  Cmd = "bedtools intersect -a \"%(f1_name)s\" -b \"%(f2_name)s\" -wa | cut -f 1-3 | sort | uniq | wc -l | cut -d \" \" -f 1" % {"f1_name":F1_name,"f2_name":F2_name}
  Count = int(subprocess.check_output(Cmd, shell=True).strip())
  return Count

def countTotalTFBS(F_name):
  F = open(F_name)
  Count = 0
  for line in F:
    Count += 1
  return(Count)

def calcRegdomLength(F_name):
   Cmd = 'awk \'BEGIN{sum=0}{sum+=$3-$2}END{print sum}\' \"%(f_name)s\"'  % {"f_name":F_name}
   Length = float(subprocess.check_output(Cmd, shell=True).strip())
   return(Length)

def binomTest(CountHit,CountTotal,Prop):
  Pval = stats.binom_test(CountHit,CountTotal,Prop)
  if float(CountTotal) > 0 and (Prop != 0):
    Fe = (float(CountHit) / float(CountTotal)) / Prop
  else:
    Fe = "na"
  return Pval, Fe

TFBS_bed_f_name = argvs[1]
total_region_f = argvs[2]


total_length = calcRegdomLength(total_region_f)
countTotal = countHitonRegdom(TFBS_bed_f_name,total_region_f)

print "gs_name\tTFBSs_total\tTFBSs_on_regdom\tPval\tFold_enrichment"

for regdom_f_name in argvs[3:]:
  regdom_name = re.sub(r'.+\/([^\/]+)\..+',r'\1',regdom_f_name)
  regdom_length = calcRegdomLength(regdom_f_name)
  prop = regdom_length / total_length
  countHit = countHitonRegdom(TFBS_bed_f_name,regdom_f_name)
  pval,fe = binomTest(countHit,countTotal,prop)
  res_l = [regdom_name,countTotal,countHit,pval,fe]
  #if countHit >= 5:
  print "\t".join([str(c) for c in res_l])
