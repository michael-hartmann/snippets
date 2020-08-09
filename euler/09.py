#!/usr/bin/python

from math import sqrt

p = 1000
for b in range(1,p):
    for a in range(1, b):
        c = sqrt(a**2+b**2)
        if c == int(c) and (a+b+int(c)) == p:
            print(a,b,c, a+b+c, a*b*c)
