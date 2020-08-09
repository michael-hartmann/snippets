from math import sqrt
from itertools import chain
 
def sieve(limit):
    is_prime = [True] * (limit >> 1)
    is_prime[0] = False
    for i in range(3, int(sqrt(limit)) + 1, 2):
        if is_prime[i >> 1]:
            for j in range((i >> 1) + i, limit >> 1, i):
                is_prime[j] = False
    #return list(chain([2], ((i << 1) + 1 for i, t in enumerate(is_prime) if t)))
    return chain([2], ((i << 1) + 1 for i, t in enumerate(is_prime) if t))
