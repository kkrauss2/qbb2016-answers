#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
#One of the machine learning packages.

df = pd.read_table( sys.argv[1], sep=" ", header=None)

n, p = df.shape

# df = df.T
#We are not transposing the matrix here

#for line in df:
#    fields = line.rstrip("\n\r").split(" ")

# x = pca.transform( df )

plt.figure()
plt.scatter( df[2], df[3] )
plt.ylabel("Principle Component 2")
plt.xlabel("Principle Component 1")
plt.title("PCA Genotype Plot")
# plt.xticks( range(len(df.columns)), df.columns, rotation = 90 )
#The rotation rotates the x values by 90 degress so they are perpendicular to the bottom of the plot.
# plt.subplots_adjust(bottom = .25)
#This moves the bottom of the plot down so you can read the entire x value which we assigned in xticks
# plt.legend()
plt.savefig("pca-genotype.png")
