def divisors(n):
    l = []
    for i in range(1,n//2+1):
        if (n%i) == 0:
            l.append(i)
    return l

def d(n):
    return sum(divisors(n))

def isamicable(n):
    dn = d(n)
    if dn != n and d(dn) == n:
        return True
    return False

if __name__ == "__main__":
    s = 0
    for n in range(1,10000):
        if isamicable(n):
            print(n)
            s += n
    
    print(s)
