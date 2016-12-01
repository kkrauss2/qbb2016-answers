#!/usr/bin/env python 

from __future__ import division 
import sys
import numpy as np
import h5py

df = open(sys.argv[1])

ctcf_positions = []

for i, line in enumerate(df):
    fields = line.rstrip("\r\n").split("\t")
    
    if fields[0] == "chrX":
        ctcf_positions.append(fields[1])
    else:
        continue
        
print ctcf_positions