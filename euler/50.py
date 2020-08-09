from prime import sieve
from itertools import count

primes     = tuple(sieve(1000000))
primes_set = set(primes)

maximum = (0,0)
for idx_start in range(0, len(primes)):
    print(idx_start, primes[idx_start])
    s = 0
    for j,i in enumerate(count(idx_start), start=1):
        s += primes[i]
        
        if s >= 1000000:
            break
        if s in primes and j > maximum[0]:
            maximum = (j,s)
            print(maximum)
