#!/usr/bin/python

from math import factorial

s = str(factorial(100))

sum = 0
for d in s:
    sum += int(d)

print sum
