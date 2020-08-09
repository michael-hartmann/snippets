from prime import sieve

def rotations(x):
    s = str(x)
    length = len(s)

    l = []
    for i in range(length):
        s = s[-1] + s[:-1]
        l.append(int(s))
    return l
        


if __name__ == "__main__":
    primes = set(sieve(1000000))

    circular = set()

    for prime in sieve(1000000):
        is_circular_prime = True
        for x in rotations(prime):
            if x not in primes:
                is_circular_prime = False
                break

        if is_circular_prime:
            circular.add(prime)

    print("total number of circular primes below 1000000:", len(circular))
