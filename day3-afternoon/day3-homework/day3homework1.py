#!/usr/bin/env python

import sys, fasta

k = int(sys.argv[3])
t = target_database = (sys.argv[1])
q = query_database = (sys.argv[2])

query_kmers = {}
target_kmer_matches = {}

for ident, sequence in fasta.FASTAReader(open(q)):
    sequence = sequence.upper()
    #print sequence - WORKS UP TO HERE
    
    #print len(sequence)
    
    for i in range(0, len(sequence) - k):
        #print i
        kmer = sequence[i : i+k]
       
        #print kmer THIS ALSO WORKS
        query_kmers [ kmer ] = i
        #if kmer in query_kmers:
            #continue
            #print "already in list"
        #else:
            #print "adding to list"
            #query_kmers.append(kmer)
            
            
for ident, sequence in fasta.FASTAReader(open(t)):
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
        print "Sequence:", kmer, "\t", "Target Position:", i_t, "\t", "Query Position:", i_q
    else:
        continue

#print query_kmers               
        
        #for ident, sequence in fasta.FASTAReader(open(t)):
            #sequence = sequence.upper()
            #for i in range(0, len(sequence) -k):
        
                #print "No match"
            #else:
                #print "Got one"
        
#for kmer in sorted(kmer_counts, key=kmer_counts.get):
    #print kmer, kmer_counts[kmer]