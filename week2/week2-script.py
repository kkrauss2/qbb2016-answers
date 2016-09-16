#!/usr/bin/env python

import sys
import fasta
import numpy as np

contig = fasta.FASTAReader(open(sys.argv[1]))

count = 0
contig_list = []
##To determine number of contigs

for identifier, sequence in contig:
    count += 1

##To determine length of contigs

    length = len(sequence)

##To create a list of contig lengths
    
    contig_list.append(length)

##To find maximum, minimum, and average
    
max_contig = max(contig_list)
min_contig = min(contig_list)
avg_contig = np.mean(contig_list)

##To sort the list from smallest to largest

contig_list.sort()

#To find the n50 of the contigs 

sum_contig = sum(contig_list)
half_g = sum_contig/2

length_so_far = 0

for item in contig_list:
    if length_so_far < half_g:
        length_so_far += item
    elif length_so_far >= half_g:
        n50 = item
        break
    else:
        continue


print "Number of Contigs:", count
print "Maximum Contig:", max_contig 
print "Minimum Contig:", min_contig 
print "Average Contig Length:", avg_contig
print "N50:", n50