from itertools import permutations

digits = [0,1,2,3,4,5,6,7,8,9]

s = 0
for (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10) in permutations(digits,10):
    if d1 == 0:
        continue

    if (d8*100+d9*10+d10) % 17:
        continue
    if (d7*100+d8*10+d9) % 13:
        continue
    if (d6*100+d7*10+d8) % 11:
        continue
    if (d5*100+d6*10+d7) % 7:
        continue
    if d6 % 5: #if (d4*100+d5*10+d6) % 5:
        continue
    if (d3+d4+d5)%3: # if (d3*100+d4*10+d5) % 3:
        continue
    if d4 % 2: #if (d2*100+d3*10+d4) % 2:
        continue

    number = int(d1*1000000000+d2*100000000+d3*10000000+d4*1000000+d5*100000+d6*10000+d7*1000+d8*100+d9*10+d10)
    s += number

print(s)
