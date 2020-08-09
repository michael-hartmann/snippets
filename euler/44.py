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

def pentagonal(n):
    return n*(3*n-1)//2

if __name__ == "__main__":
    maximum = 3000
    for j in range(1,maximum+1):
        Pj = pentagonal(j)
        for k in range(1,j+1):
            Pk = pentagonal(k)

            if is_pentagonal(Pj+Pk) >= 0 and is_pentagonal(Pj-Pk) >= 0:
                D = Pj-Pk
                print(j,k,D)

