from itertools import count

def cycle(d):
    digits = []
    lookup = {}
    n = 1
    for i in count(1):
        n *= 10
        div,n = n//d, n%d

        if n == 0:
            return []

        if n in lookup:
            return digits[lookup[n]:]

        lookup[n] = i
        digits.append(div)


print(max([(len(cycle(n)),n) for n in range(1, 1000)])[1])
