#!/usr/bin/python

from itertools import product

l = range(100,1000)
max = 0
sol = False

for x,y in product(l,l):
    p = x*y
    s = str(p)
    if s == s[::-1]:
        if p > max:
            max = p
            sol = x,y,p

print sol
