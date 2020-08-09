from math import sqrt

def isprime(n):
    for m in range(2,int(sqrt(n))+1):
        if n % m == 0:
            return False
    return True

if __name__ == "__main__":
    factor = 600851475143

    primes = []
    for n in range(2,int(sqrt(factor))+1):
        if (factor % n) == 0 and isprime(n):
            primes.append(n)

    print(max(primes))
