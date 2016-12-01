#!/usr/bin/env python 

from __future__ import division 
import sys
import numpy as np
import h5py

file = h5py.File( "enrichment-zero.heat" )
# file.keys()

counts = file['0.counts'][...]
expected = file['0.expected'][...]

# exp = np.where( expected > 0 )
where = (np.where( counts > 0 ))

# ratio = np.log( counts[cnts] / expected[cnts] )

results=np.empty(counts.shape)

results[where]= np.log(( counts[where] / expected[where] ))

#results = results[where]

# print results

df = open(sys.argv[1])

ctcf_positions = []

for i, line in enumerate(df):
    fields = line.rstrip("\r\n").split("\t")
    
    # print fields
    
    if fields[0] == "chrX":
        ctcf_positions.append(fields[1])
    else:
        continue
        

heat_map_positions = file['0.positions'][...]

# print heat_map_positions

ctcf_positions.sort()

ctcf_in_heatmap = []

#print ctcf_positions


for value in ctcf_positions:
    # print value
    # if value >= 98831147 and value <= 103425148:
    #     print value
    #     ctcf_in_heatmap.append(value)
    # else:
    #     continue
    # print value
    if int(value) < 98831147:
        continue
    if int(value) > 103425148:
        continue
    else:
        ctcf_in_heatmap.append(int(value))
    
# print ctcf_in_heatmap

# print heat_map_positions

for i, position in enumerate(ctcf_in_heatmap):
    if position in results:
        print position
    else:
        continue