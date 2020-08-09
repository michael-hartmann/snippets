from math import factorial

lookup = tuple([factorial(i) for i in range(10)])

def check(x0):
    x = x0
    s = 0
    while x:
        s += lookup[x % 10]
        x //= 10
    
    return x0 == s


if __name__ == "__main__":
    for i in range(3,100000):
        if(check(i)):
            print(i)
