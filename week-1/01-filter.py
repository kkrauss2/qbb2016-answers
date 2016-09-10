#!/usr/bin/env python

import sys
import uuid

nuc = open(sys.argv[1])

for line in nuc:
    field = line.rstrip("\r\n").split("\t")
    q_start = field[0]
    q_end = field[1]
    seq = field[2]
    if q_start != "1":
        continue
    if q_end != "10293":
        continue
    else:
        if "-" in line:
            no_dash = line.replace("-","")
            # print no_dash
            field = no_dash.rstrip("\r\n").split("\t")
            print ">" + str(uuid.uuid4()) + "\n" + str(field[2])
        else:
            good_line = line
            field =good_line.rstrip("\r\n").split("\t")
            print ">" + str(uuid.uuid4()) + "\n" + str(field[2])