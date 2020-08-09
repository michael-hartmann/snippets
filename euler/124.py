from prime import sieve

primes = list(sieve(100000))

def rad(n):
    product = 1
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            product *= p

    return product


E = list(sorted([(rad(n),n) for n in range(1,100001)]))

print(E[10000-1])
