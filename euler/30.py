def check(n):
    return n == sum(map(lambda x: int(x)**5, str(n)))

l = []
for i in range(2, 1000000):
    if check(i):
        print(i)
        l.append(i)

print()
print(sum(l))
