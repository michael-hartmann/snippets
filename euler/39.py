#!/usr/bin/python

from math import sqrt

def f(p):
    n = 0
    for b in range(1,p):
        for a in range(1, b):
            c = p-a-b
            if a*a+b*b-c*c == 0:
                n += 1
                #print(a,b,c, a+b+c, a*b*c)
    return n

if __name__ == "__main__":
    maximum = (-1,-1)

    for p in range(1,1001):
        fp = f(p)
        if fp > maximum[1]:
            maximum = (p, fp)

    print(maximum)
