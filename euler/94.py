import math

def sqrt(a):
    x = int(round(math.sqrt(a)))

    if x*x == a:
        return True, x
    else:
        return False, x


if __name__ == "__main__":
    s = 0
    a = -1

    print("# a, c, A, U")
    while True:
        a += 2

        for c in (a-1, a+1):
            isinteger,value = sqrt(4*a*a-c*c)
            #print(isinteger, 4*a*a-c*c, math.sqrt(4*a*a-c*c))

            # A * 4
            A4 = value*c

            U = a+a+c
            if U >= 1000000000:
                break

            if isinteger and A4 and A4 % 4 == 0:
                A = A4//4
                s += U
                print(a, c, A, U)
                #print(a, c, sqrt(a**2-(c/2)**2))

    print(s)
