from itertools import count

def digit_sum(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


if __name__ == "__main__":
    maximum = 10000000000000000000

    max_base = len(str(maximum))*9

    l = []
    for base in range(2, max_base+1):
        for power in count(1):
            number = base**power
            if number > maximum:
                break
            if number >= 10 and base == digit_sum(number):
                l.append(number)

    for i,v in enumerate(sorted(l)):
        print("a%d: %d" % (i+1, v))
