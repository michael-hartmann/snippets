from math import sqrt

def fn(n):
    sqrt5 = sqrt(5)
    a = (1+sqrt5)/2
    b = (1-sqrt5)/2

    return (a**n-b**n)/sqrt5



for n in range(100):
    x = fn(n)
    print(n, x, x > 4000000)
