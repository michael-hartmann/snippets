from prime import sieve

primes = set(sieve(2100000))

def primesequence(f):
    n = 0
    while True:
        if f(n) not in primes:
            return n
        n += 1

if __name__ == "__main__":
    maximum = (0,0,0)

    for a in range(-999,999+1):
        for b in range(-1000,1000+1):
            f = lambda n: n*(n+a)+b
            x = primesequence(f)
            if x > maximum[0]:
                maximum = (x,a,b)


    print()
    print(maximum)
    print(maximum[1]*maximum[2])
