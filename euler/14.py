#!/usr/bin/python

max,index = 0, -1

for start in range(1,1000000):
    l = [start]

    if start % 10000 == 0:
        print start/10000

    while l[-1] != 1:
        last = l[-1]
        if (last % 2) == 0:
            l.append(last/2)
        else:
            l.append(3*last+1)

    if len(l) > max:
        max,index = len(l),start

print max,index
