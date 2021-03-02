#!/usr/bin/env python

import sys
import numpy as np
import statistics

argvs = sys.argv

gs_f = open(argvs[1])
gsea_f = open(argvs[2])

max_res_num = 10
max_overlap = 0.5

def jaccard(x, y):
    """
    Jaccard index
    Jaccard similarity coefficient
    https://en.wikipedia.org/wiki/Jaccard_index
    """
    x = frozenset(x)
    y = frozenset(y)
    return len(x & y) / float(len(x | y))

gs_f.next()
gs_d = {}
for line in gs_f:
  line = line.strip().split("\t")
  gs_name,ens_Id,symbol = line
  if gs_name not in gs_d:
    gs_d[gs_name] = []
  gs_d[gs_name].append(ens_Id)


gsea_d = {}
gsea_f.next()
for line in gsea_f:
  line = line.strip().split()
  gs_name = line[0]
  padj = line[-1]
  OR = line[1]
  if padj != "NA" and OR != "NA":
    padj = float(padj)
    OR = float(OR)
    if padj < 0.05:
      gsea_d[gs_name] = OR



i = 0
for gs_name, OR in sorted(gsea_d.items(), key=lambda x: -x[1]):
  if OR > 0:
    if i == 0:
      res_l = [gs_name]
    else:
      if len(res_l) < max_res_num:
        sim_l = []
        for high_gs_name in res_l:
          ens_Id_l = gs_d[gs_name]
          high_ens_Id_l = gs_d[high_gs_name]
          sim = jaccard(ens_Id_l,high_ens_Id_l)
          sim_l.append(sim)
        if max(sim_l) < max_overlap:
          res_l.append(gs_name)
    i += 1

print "gs_name\tOR"
for gs_name in res_l:
  OR = gsea_d[gs_name]
  print gs_name + "\t" + str(OR)

