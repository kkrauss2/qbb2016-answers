#!/usr/bin/env python

"""
This program will go through the ctab file inserted on the command
line as argument number one. It will then extract the chromsome number,
transcript name, a new start sign which is 500 nucleotide bases before the
original start site and an end site with is a 500 nucleotide bases after the
start site.

This program takes into account both positive and negative strands of DNA
in the ctab file and determines the start and end sites appropriately.

The output is returned as a .bed file without headers, so do note that
the columns are chromosome name, start point, end point, and t_name in that 
order
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_ctab = pd.read_table(sys.argv[1])

df_roi = df_ctab["chr"].str.contains( "211000" )
df_ctab = df_ctab[~df_roi] 

#print df_ctab ---THIS WORKS SO FAR

for row in df_ctab.itertuples():
    chrm = row[2]
    t_name = row[6]
    if "+" in row[3]:
        start = row[4] - 500
        end = row[4] + 500
    if "-" in row[3]:
        start = row[5] + 500
        end = row[5] - 500
        
    print chrm + "\t" + str(start) + "\t" + str(end) + "\t" + t_name