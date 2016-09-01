#!/usr/bin/env python

"""
User can use this program to compare two SRR files against each other in an
MA-plot. SRR files should be added in the command line in any order.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_ctab893 = pd.read_table(sys.argv[1])
df_ctab915 = pd.read_table(sys.argv[2])

df_roi1 = df_ctab893[ "FPKM" ] 

x = df_roi1.values

df_roi2 = df_ctab915[ "FPKM" ]

y = df_roi2.values

m = np.log2(x/y)
a = (np.log2(x*y))/2

plt.figure()
plt.scatter(a, m, alpha=0.2)
plt.title("MA-plot comparing 893 with 915")
plt.xlabel("A")
plt.ylabel("M")
plt.savefig("homework3.png")
plt.close