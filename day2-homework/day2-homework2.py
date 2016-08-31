#!/usr/bin/env python


#Within this document, there are two unique options which can be run. If the program is typed into command and followed with "-h", then the default "." as seen in option 2 of the second homework value will be printed (see comments below for more information). If the program is typed into command and follwed with "-a", then the nothing will be printed as requested by option 1 of the second homework question (see below comments for more details).

import sys

#The below portion is the creation of the dictionary and the assigning of variables to values from the file made in the previous homework exercise

opt = sys.argv[1]

my_dict = {}
for line in open("/Users/cmdb/qbb2016-answers/day2-homework/day2-homework1"):
    c = line.split()
    fly_id = c[1]
    ac = c[0]
    my_dict[fly_id] = ac
    

#The below portion compares the ctab document to the document which was created in exercise 1. If the value exists in the dictionary, the dictionary will be replaced with the new value, otherwise the flybase ID will still be printed.  

#This prints the new entry and the line of the ctab file (rna seq data of drosophila embryos) if it is found in the dictionary. Otherwise a period is printed  

#This is the default value option from subsection 2 of the assignment
if opt == "-h":
    for line in open("/Users/cmdb/qbb2016-answers/day1-homework/t_data.ctab"):    
        f = line.split()
        d = f[8]
        if d in my_dict:
            print my_dict[d] and line
        else:
            print "."

#The below portion compares the ctab document ot the document which was created in exercise 1. If the value exists in the dictionary, the dictionary will be replaced with the new value, otherwise the flybasde ID will still be printed.

#This prints the new entry and the line of the ctab file if it is found in the dictionary. Otherwise nothing is printed.

#This is the print nothing option from subsection 1 of the assignment     
   
if opt == "-a":   
    for line in open("/Users/cmdb/qbb2016-answers/day1-homework/t_data.ctab"):    
        f = line.split()
        d = f[8]
        if d in my_dict:
            print my_dict[d] and line
        else:
            continue
    