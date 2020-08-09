#!/usr/bin/python

from prime import sieve

primes = sieve(120000)

len = 0
for x in primes:
    len += 1
    if len == 10001:
        print(x)
