#!/usr/bin/python

sum = 0
fh = open("13.dat", "r")
for line in fh:
    sum += int(line)

s = str(sum)
print s[0:10]
