from prime import sieve
 
sum = 0
for p in sieve(2000000):
    sum += p

print(sum)
