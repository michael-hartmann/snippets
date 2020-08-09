from prime import sieve

maximum = 1000000
primes = set(sieve(maximum))

def check(x):
    s = str(x)

    for i in range(1,len(s)):
        p1 = s[:i]
        if int(p1) not in primes:
            return False
        p2 = s[i:]
        if int(p2) not in primes:
            return False
    
    return True


if __name__ == "__main__":
    s = 0
    for prime in primes:
        if check(prime) and prime >= 10:
            s += prime


    print(s)
