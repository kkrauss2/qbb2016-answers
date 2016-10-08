#!/usr/bin/env python

from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import sys

for fname in sys.argv[1:]:
    f = open(sys.argv[1])

    p_value = []

    for i, line in enumerate(f):
        if i == 0:
            continue
        else:
            fields = line.rstrip("\n\r").split()
            p = -np.log10( float(fields[8]) )
            p_value.append(p)

    y = np.array(p_value)
    x = np.array(range(len(p_value)))

    threshold = -np.log10(10 ** -5)

    loy = y[y < threshold]
    hiy = y[y >= threshold]

    lox = x[y < threshold]
    hix = x[y >= threshold]
        
    # print p_value
    treatment = fname.split(".")[1]

    plt.figure()
    plt.scatter(lox, loy, edgecolor = "None")
    plt.scatter(hix, hiy, edgecolor = "None", color = 'r')
    plt.axhline(5, color = 'r', linestyle = ':')
    plt.xlabel("SNP")
    plt.ylabel("-log")
    plt.title("Manhattan Plot of " + treatment)
    plt.savefig("Plot-of-" + treatment + ".png")