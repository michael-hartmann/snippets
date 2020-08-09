def divisors(n):
    l = []
    for i in range(1,n//2+1):
        if (n%i) == 0:
            l.append(i)
    return l

def d(n):
    return sum(divisors(n))

# True if n is an abundant number
def isabundant(n):
    return d(n) > n

if __name__ == "__main__":
    limit = 28123

    # get all abundant numbers <= limit
    abundant = []
    for n in range(1,limit+1):
        if isabundant(n):
            abundant.append(n)

    # compute all sums of two abundant numbers < limit (and a few above)
    sum_of_two_abundant_numbers = {}
    for x in abundant:
        for y in abundant:
            sum_of_two_abundant_numbers[x+y] = True

    # compute sum of all numbers that can not be expressed as sum of two
    # abundant numbers
    s = 0
    for n in range(1,limit+1):
        if n not in sum_of_two_abundant_numbers:
            s += n

    print(s)
