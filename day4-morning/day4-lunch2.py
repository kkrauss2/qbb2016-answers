#!/usr/bin/env python

"""
This program will take in 2 different ctab files which should be
typed in the command line after the function in any order. This program
also requires the fourth thing in the command line typed after both ctab files
to be the window size of the rolling mean (ex: 200).

The program will then compare the rolling mean of the FPKM values on both
ctab files on chromosomes 2L, 2R, 3L, 3R, 4, and X.

Images will be returned for each chromosomes comparing the rolling means on
each image. The ctab files will be labeled as Sample 1 and Sample 2 respective 
to the order in which they are typed on the command line."""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])
window = int(sys.argv[3])

chromosomes = ["2L", "2R", "3L", "3R", "4", "X"]

for x in chromosomes:
    df_roi1 = df1[ "chr" ] == x
    df_chrom1 = df1[df_roi1]
    df1_for_chrom = df_chrom1[ "FPKM" ].rolling(window).mean()

    df_roi2 = df2[ "chr" ] == x
    df_chrom2 = df2[df_roi2]
    df2_for_chrom = df_chrom2[ "FPKM" ].rolling(window).mean()

    plt.figure()
    plt.plot(df1_for_chrom, label="Sample 1") 
    plt.plot(df2_for_chrom, label="Sample 2")
    plt.legend()
    plt.ylabel("Rolling Mean of FPKM")
    plt.xlabel("Position")
    plt.title( "Chromosome:" + x + "FPKM rolling mean (size = " + str(window) + ")" )
    plt.savefig( "rollingmeanplots" + x + ".png" )
    plt.close()