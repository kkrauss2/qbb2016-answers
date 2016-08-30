#!/usr/bin/env python

import sys

count = 0
number = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    elif line.split()[4] != "*":
        var = line.split()[4]
        count = count + int(var)
        number = number + 1
    else:
        break
                
print float(count / number)
                
                