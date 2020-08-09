from scipy.special import binom

terms = 0
for n in range(0,101):
    for r in range(n+1):
        if binom(n,r) > 1000000:
            terms += 1

print(terms)
