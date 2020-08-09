from prime import sieve
from itertools import count

maximum = 1000000
primes_list = tuple(sieve(maximum))

def factorize(n):
    factors = []
    for prime in primes_list:
        if prime > n:
            return factors

        while n % prime == 0:
            factors.append(prime)
            n = n//prime

def number_of_dividors_square(n):
    factors = {}
    for factor in factorize(n):
        factors[factor] = factors.get(factor, 0) + 1

    dividors = 1
    for factor,multiplicity in factors.items():
        dividors *= 2*multiplicity+1

    return dividors


for n in count(1):
    solutions = (number_of_dividors_square(n)+1)//2
    if solutions > 1000:
        print(n, solutions)
        exit(0)
