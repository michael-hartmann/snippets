from prime import sieve

primes = list(sieve(10000000))

def remainder(n):
    pn = primes[n-1]
    return ((pn-1)**n+(pn+1)**n) % (pn*pn)


for k in range(21001, 100000):
    x = remainder(k)
    if x > 10000000000:
        print(k, x)
        break
