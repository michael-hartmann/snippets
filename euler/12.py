def Tn(n):
    return (n*(n+1))//2

def factors(n):
    l = []
    for i in range(1,n+1):
        if (n%i) == 0:
            l.append(i)
    return l

if __name__ == "__main__":
    n = 1
    while True:
        x = Tn(n)
        l = factors(x)

        print(x)
        if len(l) > 500:
            print(n, x, len(l))
            break

        n += 1
