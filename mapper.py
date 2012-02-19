#!/usr/bin/python
import sys


def emit(*args):
    print '\t'.join(args)

for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    if len(data) >= 5 and data[4]:
        emit(data[4], "1")
