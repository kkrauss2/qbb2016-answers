#!/usr/bin/env python

import sys

narrow = open(sys.argv[1])

for line in narrow:
    field = line.rstrip("\r\n").split("\t")
    
    print field[0]+"\t"+field[1]+"\t"+field[2]+"\t"+field[3]+"\t"+field[4]+"\t"+field[5]
    