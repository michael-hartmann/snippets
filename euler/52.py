def sort(s):
    s = str(s)
    return "".join(sorted(s))

def check(x):
    sx = sort(x)
    if sort(2*x) != sx:
        return False
    if sort(3*x) != sx:
        return False
    if sort(4*x) != sx:
        return False
    if sort(5*x) != sx:
        return False
    if sort(6*x) != sx:
        return False
    return True


for i in range(1,100000000):
    if check(i):
        print(i)
        break
