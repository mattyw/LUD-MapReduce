#!/usr/bin/python
import sys
from collections import defaultdict

reducer = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    reducer[key] += int(value)

for key,value in reducer.iteritems():
    print '%s\t%s\n' %(key, value)
