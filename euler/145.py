def check(n):
    if n % 10 == 0:
        return False
    r = int(str(n)[::-1])
    s = str(n+r)

    if "2" in s or "4" in s or "6" in s or "8" in s or "0" in s:
        return False
    return True


total = 0
maximum = 1000000000
for n in range(1, maximum):
    if n % 10000000 == 0:
        print(n/maximum*100)
    if check(n):
        total += 1


print()
print(total)
