#!/usr/bin/python

sum  = 0
sum2 = 0

for x in range(1,101):
    sum  += x
    sum2 += x**2

print sum**2, sum2, sum**2-sum2
