#!/usr/bin/python

d = {}
min = 2
max = 100
for a in range(min, max+1):
    for b in range(min, max+1):
        d[a**b] = True

print len(d.keys())
