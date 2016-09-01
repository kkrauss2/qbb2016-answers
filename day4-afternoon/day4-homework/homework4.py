#!/usr/bin/env python

"""
User can utilize this code to feed in a ctab file as the first argument and 
generate a gaussian kernel density plot of the FPKMs for that data.

Note that this program does filter out FPKM = 0, therefore it is likely to
observe a skew.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df_ctab893 = pd.read_table(sys.argv[1])

df_roi1 = df_ctab893[ "FPKM" ] 

x = df_roi1.values

density = gaussian_kde(x)
#works up to here

xs = np.linspace(-8, 250, 200)

plt.figure()
plt.plot(xs, density(xs))
plt.title("Density plot of FPKM values for 893")
plt.xlabel("FPKM")
plt.ylabel("Density")
plt.savefig("homework4.png")
plt.close