#!/usr/bin/env python

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, leaves_list
from scipy.cluster.hierarchy import leaves_list as leafy
from scipy.spatial.distance import pdist
from scipy.cluster.vq import kmeans2 as kmeans
import numpy as np
import csv
import pydendroheatmap as pdh
try: import cPickle as pickle
except: import pickle
import pandas as pd

data = sys.argv[1] 

f = open(data)
# print f

cells = []
genes = []
table = []
cfu = []


for i, line in enumerate(f):
    fields = line.split('\t')
    # print fields
    if i == 0:
        cells = fields[1:]
    # elif fields == 1:
        # cfu.append( [float(x) for line in fields[1]] )
    else:
        genes.append(fields[0])
        table.append( [float(x) for x in fields[1:]] )
        # cfu.append( [float(x) for x in fields[1:1]] )

# for i, line in enumerate(f):
#     fields = line.split('\t')
#     if i > 0:
#         cfu_data.append( [float(x) for x in fields[1]] )
        
    
matrix = np.array(table)

# print matrix

Z = linkage(matrix)

leaves = leafy(Z)

# print leaves

trans = np.transpose(matrix)
ZZ = linkage(trans)

leaves_flip = leafy(ZZ)

# print trans

plt.figure()
dendrogram(ZZ, labels=cells)
plt.title('Hierarchical Clustering Dendogram')
plt.xlabel('Cell Type')
# myticks = ['CFU', 'poly', 'unk', 'mys', 'int', 'mid']
plt.ylabel('Distance')
plt.tight_layout()
plt.savefig("Dendrogram.png")
plt.close()

plt.figure()
dendrogram(Z, labels=genes)
plt.title('Hierarchical Clustering Dendogram')
plt.xlabel('Gene Names')
# myticks = ['CFU', 'poly', 'unk', 'mys', 'int', 'mid']
plt.ylabel('Distance')
plt.tight_layout()
plt.savefig("Dendrogram-genes.png")
plt.close()


# heatmap_array = pickle.load(matrix)
# top_dendy = pickle.load(Z)
# side_dendy = pickle.load(ZZ)

matrix = matrix [ leaves, : ]
matrix = matrix [ :, leaves_flip]

heatmap = pdh.DendroHeatMap(heat_map_data = matrix, left_dendrogram = Z, top_dendrogram = ZZ)
heatmap.title = 'Cell Type vs Gene Heat Map'
heatmap.column_labels = ['CFU', 'poly', 'unk', 'mys', 'int', 'mid']
heatmap.export("Heatmap.png")
plt.close()

centers, km = kmeans(matrix[:,[0,2]], 8, iter=10, thresh=1e-05, minit='random', missing='warn')

# print km
#
color_vals = []

for label in km:
    if label == 0:
        colors = 'blue'
    if label == 1:
        colors = 'green'
    if label == 2:
        colors = 'yellow'
    if label == 3:
        colors = 'orange'
    if label == 4:
        colors = 'purple'
    if label == 5:
        colors = 'cyan'
    if label == 6:
        colors = 'black'

    color_vals.append(colors)

plt.figure()
plt.title('Poly vs CFU Gene Expression')
plt.xlabel('Poly')
plt.ylabel('CFU')
plt.scatter(matrix[:, 2],matrix[:, 0], c = color_vals)
plt.savefig('Poly_vs_CFU.png')
plt.close

cfu_data = []

# for fields in f:
#     fields = line.split('\t')
#     if fields == 1:
#         early_mean_1.append(lines)

for i, line in enumerate(f):
    fields = line.split('\t')
    if i == 0:
        continue
    else:
        cfu_data.append( [float(x) for x in fields[1:]] )



# print cfu_data
#     if i == 0:
#         cells = fields[1:]
#     else:
#         genes.append(fields[0])
#         table.append( [float(x) for x in fields[1:]] )