from math import sqrt

def is_pentagonal(a):
    root = sqrt(1+24*a)    
    if root != int(root):
        return -1

    root = int(root)
    n = (1+root)/6

    if n != int(n):
        return -1
    else:
        return int(n)


def is_hexagonal(a):
    root = sqrt(1+8*a)    
    if root != int(root):
        return -1

    root = int(root)
    n = (1+root)/4

    if n != int(n):
        return -1
    else:
        return int(n)

def Tn(n):
    return n*(n+1)//2

if __name__ == "__main__":
    n = 286
    while True:
        x = Tn(n)
        if is_pentagonal(x) > 0 and is_hexagonal(x) > 0:
            print(n, x)
            break
        n += 1
