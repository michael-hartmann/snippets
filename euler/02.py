#!/usr/bin/python

fib = 1,2
max = 4e6

sum = 0

while True:
    if fib[0] > max:
        break

    if (fib[0] % 2) == 0:
        sum += fib[0]

    fib = fib[1], fib[0]+fib[1]

print sum
