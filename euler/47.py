from prime import sieve
from itertools import count

maximum = 1000000
primes_list = tuple(sieve(maximum))

def factorize(n):
    factors = 0
    for prime in primes_list:
        if prime > n:
            return factors

        flag = False
        while n % prime == 0:
            flag = True
            n = n//prime

        if flag:
            factors += 1


consecutive = 0
for i in count(647):
    if factorize(i) > 3:
        consecutive += 1

        if consecutive == 4:
            print(i-3, i-2, i-1, i)
            exit(0)
    else:
        consecutive = 0
