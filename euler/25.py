#!/usr/bin/python

fib = (1,1)
i = 2

while True:
    if fib[0] >= 10**999:
        print i,fib[0], len(str(fib[0]))
        break
    i += 1
    fib = fib[0]+fib[1], fib[0]
