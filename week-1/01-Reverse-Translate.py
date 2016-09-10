#!/usr/bin/env python

import sys
import fastaP
import itertools


nuc = fastaP.FASTAReader(open(sys.argv[1]))
prot = fastaP.FASTAReader(open(sys.argv[2]))

amino_acids = []
nucleotides = []

for aa in prot:
    amino_acids.append(aa)
    
for nt in nuc:
    nucleotides.append(nt)
    
for thing in itertools.izip(nucleotides, amino_acids):
    s = []
    n = 0
    nuc_s = thing[0][1]
    pro_s = thing[1][1]
    
    for aa in pro_s:
        if aa == "-":
            s.append("---")
        else:
            codon = nuc_s[n:n+3]
            n += 3
            s.append(codon)
        
    print ">"+thing[0][0]
    print "".join(s)    