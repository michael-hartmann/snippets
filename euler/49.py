from itertools import permutations
from prime import sieve

primes = set(sieve(10000))
sequences = set()

for i in range(1000,10000):
    d1 = (i // 1000) % 10
    d2 = (i // 100) % 10
    d3 = (i // 10) % 10
    d4 = i % 10

    primes_in_permutations = set()
    for permutation in permutations([d1,d2,d3,d4],4):
        number = permutation[0]*1000+permutation[1]*100+permutation[2]*10+permutation[3]
        if number in primes:
            primes_in_permutations.add(number)

    if len(primes_in_permutations) > 2:
        sorted_primes_in_permutations = list(sorted(primes_in_permutations))
        for i0,i1,i2 in permutations(range(len(sorted_primes_in_permutations)), 3):
            if not i0<i1<i2:
                continue

            q1,q2,q3 = sorted_primes_in_permutations[i0], sorted_primes_in_permutations[i1], sorted_primes_in_permutations[i2]

            if (q3-q2) == (q2-q1) and len(str(q1)) == 4 and len(str(q2)) == 4 and len(str(q3)) == 4:
                t = (q1,q2,q3)
                sequences.add(t)


for sequence in sequences:
    print(sequence, ":", "".join(map(str, sequence)))
