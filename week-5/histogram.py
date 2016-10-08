#!/usr/bin/env python

from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

f = open(sys.argv[1])

allele_freq = []

for i,line in enumerate(f):
    if line[0]=="#":
        continue
    else:
        fields = line.rstrip("\n\r").split("\t")[ 9: ]
        row = [int(x) for x in fields]
        v = sum(row)/len(row)
        allele_freq.append(v)
    
plt.figure()
plt.hist(allele_freq, 30)
plt.xlabel("Frequency")
plt.ylabel("Number of SNPS")
plt.title("Histogram of SNP Frequency")
plt.savefig("SNP-Freq-Histogram.png")