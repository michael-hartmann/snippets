#!/usr/bin/python

sum = 0
for x in range(1,1001):
    sum += x**x

s = str(sum)
print s[-10:]
