#!/usr/bin/python

from math import sqrt

for b in range(1,1000):
    for a in range(1, b):
        c = sqrt(a**2+b**2)
        if c == int(c) and (a+b+int(c)) == 1000:
            print a,b,c, a+b+c, a*b*c
