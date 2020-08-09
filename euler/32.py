from itertools import permutations

s = set()
for permutation in permutations("123456789"):
    for i in range(1, 9):
        for j in range(i+1,9):
            m1 = int("".join(permutation[:i]))
            m2 = int("".join(permutation[i:j]))
            p  = int("".join(permutation[j:]))

            if m1*m2 == p:
                s.add(p)



print(sum(s))
