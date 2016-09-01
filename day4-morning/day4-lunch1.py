#!/usr/bin/env python

"""
To use this function, run the function and as 
argument one insert one ctab data file and for argument two, 
insert a second ctab file to compare against.


This will generate a boxplot for the data in the two ctab
files comparing the FPKM values of each sample
and map it with the log value of the FPKM
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_ctab893 = pd.read_table(sys.argv[1])
df_ctab915 = pd.read_table(sys.argv[2])

# if df_ctab893[ "gene_name"] == "sxl":
df_roi893 = df_ctab893[ "gene_name" ] == "Sxl"
df_sxl893 = df_ctab893[ df_roi893 ]
df_FPKM893 =  df_sxl893[ "FPKM" ] > 0 
df_exp893 = df_sxl893[ df_FPKM893 ]
# else:
#     continue

# if df_ctab915[ "gene_name"] == "sxl":
df_roi915 = df_ctab915[ "gene_name" ] == "Sxl"
df_sxl915 = df_ctab915[ df_roi915 ]
df_FPKM915 = df_sxl915["FPKM"] > 0
df_exp915 = df_sxl915[ df_FPKM915 ]
# print df_exp915
# else:
#     continue

# print "Merging"
# df_overlap = pd.merge(df_exp893, df_exp915, on="gene_name")
# print df_overlap

import numpy as np

samples = ["SRR072893", "SRR072915"]


plt.figure()
plt.title("Log of FPKM for Sxl isoforms in both SRR072893 and SRR072915")
plt.boxplot([df_exp893["FPKM"],df_exp915["FPKM"]], labels=samples)
plt.semilogy()
plt.ylabel("log(FPKM)")
plt.xlabel("Samples")
plt.show()
plt.savefig("homework1.png")
plt.close()
