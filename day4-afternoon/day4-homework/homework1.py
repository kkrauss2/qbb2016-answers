#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <metadata.csv> <replicates> <ctab.dir>
e.g. ./01-timecourse.py samples.csv replicates.csv ~/data/results/stringtie
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_meta = pd.read_csv(sys.argv[1])
df_replicates = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]

fem_Sxl = []
male_Sxl = []
fem_Sxl_r = []
male_Sxl_r = []

df_roi_f = df_meta[ "sex" ] == "female"
for sample in df_meta[df_roi_f][ "sample" ]:
    filename_f = ctab_dir + "/" + sample + "/t_data.ctab"
    df_f = pd.read_table(filename_f)

    df_roi_f = df_f["t_name"] == "FBtr0331261"
    fem_Sxl.append(df_f[df_roi_f]["FPKM"].values)
    
df_roi_m = df_meta[ "sex" ] == "male"
for sample in df_meta[df_roi_m]["sample"]:
      filename_m = ctab_dir + "/" + sample + "/t_data.ctab"
      df_m = pd.read_table(filename_m)
      
      df_roi_m = df_m["t_name"] == "FBtr0331261"
      male_Sxl.append(df_m[df_roi_m]["FPKM"].values)

df_roi_fr = df_replicates[ "sex" ] == "female"      
for replicate in df_replicates[df_roi_fr][ "sample" ]:
    filename_fr = ctab_dir + "/" + replicate + "/t_data.ctab"
    df_fr = pd.read_table(filename_fr)
    
    df_roi_fr = df_fr["t_name"] == "FBtr0331261"
    fem_Sxl_r.append(df_fr[df_roi_fr]["FPKM"].values)

df_roi_mr = df_replicates[ "sex" ] == "male"      
for replicate in df_replicates[df_roi_mr][ "sample" ]:
    filename_mr = ctab_dir + "/" + replicate + "/t_data.ctab"
    df_mr = pd.read_table(filename_mr)
    
    df_roi_mr = df_mr["t_name"] == "FBtr0331261"
    male_Sxl_r.append(df_mr[df_roi_mr]["FPKM"].values)

x_axis = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
# y_axis = ["0", "50", "100", "150", "200", "250", "300"]

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.arange(0, 301, 50)
# y = np.array([0, 50, 150, 200, 250, 300])
plt.figure()
plt.xticks(x, x_axis)
plt.yticks(y)
plt.ylim(0, 301)
# axes = plt.gca()
# plt.axes.set_ylim([0, 300])
plt.plot(fem_Sxl, 'r-')
plt.plot(male_Sxl, 'b-')
plt.plot([4,5,6,7], fem_Sxl_r, 'r.')
plt.plot([4,5,6,7], male_Sxl_r, 'b.')
plt.ylabel("mRNA abundance (RPKM)")
plt.xlabel("developmental stage")
plt.title("Sxl")

plt.savefig("homework1.png")
plt.close()