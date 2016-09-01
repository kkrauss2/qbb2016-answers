#!/usr/bin/env python

import sys, fasta

k = int(sys.argv[3])
t = target_database = (sys.argv[1])
q = query_database = (sys.argv[2])

query_kmers = {}

kmer_length = []

for ident, sequence in fasta.FASTAReader(open(q)):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i : i+k]
        query_kmers [ kmer ] = i
    query_sequence = sequence


for ident, sequence in fasta.FASTAReader(open(t)):
    target_kmer_matches = {}
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i : i+k]
        
        if kmer in query_kmers:
            target_kmer_matches[ kmer ] = i
        else:
            continue
        
    for kmer in query_kmers:
        if kmer in target_kmer_matches:
            i_q = query_kmers[kmer]
            i_t = target_kmer_matches[kmer] 
            #print i_q, i_t
            #print len(sequence)
          
            s = kmer
          
            while True:
                i_q += 1
                i_t += 1
                if query_sequence[i_q] != sequence[i_t]:
                    break
                elif i_q + 1 == len(query_sequence) or i_t + 1 == len(sequence):
                    break
                s = sequence[i_t] + s               
                    
            while True:
                i_q -= 1
                i_t -= 1
                if query_sequence[i_q] != sequence[i_t]:
                    break
                elif i_q == 0 or i_t == 0:
                    break
                s = sequence[i_t] + s
                kmer_length.append(s)
                
print sorted(kmer_length, key=len, reverse=True)

                
