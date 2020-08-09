from prime import sieve
from math import sqrt, ceil
from itertools import count, combinations
from functools import reduce

maximum = 1000000
primes_list = tuple(sieve(maximum))
primes_set = set(primes_list)

def factorize(n):
    factors = []
    for prime in primes_list:
        if prime > n:
            return factors

        while n % prime == 0:
            factors.append(prime)
            n = n//prime

def dividors(factors):
    s = set()
    factors.append(1)
    mul = lambda a,b: a*b
    for r in range(1, len(factors)+1):
        for c in combinations(factors, r):
            s.add(reduce(mul, c))
    return s

def minmax(a,b):
    if a > b:
        return b,a
    else:
        return a,b

def solutions(n):
    n2 = n*n
    s = set()
    factors = factorize(n)
    factors = factors+factors
    for t in dividors(factors):
        x = n + t
        y = n2//t + n
        s.add(minmax(x,y))
    return s


for n in range(4,20):
    s = solutions(n)
    print(n, len(s))
