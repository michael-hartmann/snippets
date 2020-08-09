def foo(l1):
    l2 = []

    for l in l1:
        last = l[-1]
        for elem in l:
            l2.append(l + [last+elem])

    return l2


if __name__ == "__main__":
    multiplications = {}

    def update(ll):
        for l in ll:
            power = l[-1]
            length = len(l)-1
            
            if power not in multiplications or multiplications[power] > length:
                multiplications[power] = length
        

    l = [[1]]
    update(l)
    for i in range(1,10+1):
        l = foo(l)
        update(l)

    for key in sorted(multiplications):
        print(key, multiplications[key])

    s = 0
    for i in range(1,201):
        if i == 191:
            s+=11
        else:
            s += multiplications[i]

    print(s)
