from itertools import permutations
from prime import sieve

def pandigital_numbers(n):
    digits = range(1,n+1)
    for d in permutations(digits,n):
        length = len(d)
        number = 0
        for i in range(n):
            number += d[i]*10**(length-i-1)
        yield number


primes = {key: True for key in list(sieve(1000000000))}

l = []
for n in reversed(range(1,9+1)):
    for number in pandigital_numbers(n):
        if number in primes:
            l.append(number)

print(max(l))
