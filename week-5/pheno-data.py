#!/usr/bin/env python

import sys
f = open(sys.argv[1])

for i, line in enumerate(f):
    if i == 0:
        print "FID\tIID"+line.rstrip()
    else:
        fields = line.rstrip("\n\r").split("\t")

        new_field0 = fields[0].split("_")
        new_row = new_field0 + fields[1:]
        print "\t".join(new_row)
    