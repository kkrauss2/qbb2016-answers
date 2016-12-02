#!/usr/bin/env python


from __future__ import division

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, leaves_list
from scipy.cluster.hierarchy import leaves_list as leafy
from scipy.spatial.distance import pdist
from scipy.cluster.vq import kmeans2 as kmeans
from scipy.stats import ttest_ind, ttest_ind_from_stats
from scipy.special import stdtr
from scipy import stats
import itertools
import numpy as np
import csv
import pydendroheatmap as pdh
try: import cPickle as pickle
except: import pickle
import pandas as pd
from statsmodels.stats.weightstats import ttest_ind as ttest

data = sys.argv[1] 

f = open(data)

##Early stages - CFU, mys
##Late stages - Poly, unk

gene_names = []
gene_positions = []
cfu = []
mys = []
poly = []
unk = []

genes = {}

for i, line in enumerate(f):
    if i == 0:
        continue
    else:
        field = line.split('\t')
        gene_names.append(field[0])
        cfu.append(field[1])
        mys.append(field[5])
        poly.append(field[2])
        unk.append(field[3])
        gene_positions.append(i)
    
genes = dict(itertools.izip(gene_positions, gene_names))

# print genes

early = []
late = []

cfu_array = np.array(cfu, dtype = np.float)
mys_array = np.array(mys, dtype = np.float)

avg_early = (cfu_array + mys_array)/2

early.append(avg_early)

poly_array = np.array(poly, dtype = np.float)
unk_array = np.array(unk, dtype = np.float)

avg_late = (poly_array + unk_array)/2

late.append(avg_late)


early_array = np.array(early, dtype = np.float)
late_array = np.array(late, dtype = np.float)

ratio = []

temp_ratio = (early_array / late_array)
ratio.append(temp_ratio)

# print ratio

up_genes = []
up_genes_position = []
down_genes = []
down_genes_positions = []
not_sig_genes = []
not_sig_genes_positions = []
for position, value in enumerate(np.nditer(ratio)):
    if value >= 2.0:
        up_genes.append(value)
        up_genes_position.append(position)
    elif value <= 0.5:
        down_genes.append(value)
        down_genes_positions.append(position)
    else:
        not_sig_genes.append(value)
        not_sig_genes_positions.append(position)

# print up_genes

up_genes_array = np.array(up_genes, dtype = np.float)
down_genes_array = np.array(down_genes, dtype = np.float)

# print up_genes_array

up_gene_names = []
down_gene_names = []
not_sig_names = []

for position, gene, in genes.items():
    if position in up_genes_position:
        up_gene_names.append(gene)
    elif position in down_genes_positions:
        down_gene_names.append(gene)
    else:
        not_sig_names.append(gene)
        
# print up_gene_names

t, p = ttest_ind(early_array, late_array, equal_var=False)

print t

##I have been trying to get this t-test to work. I know that the problem is that I am giving it an array of averages and it wants to be able to find the averages on its own, but I cannot figure out how to get around this. Since I couldn't get past this, I couldn't perform the Panther part of this exercise. 