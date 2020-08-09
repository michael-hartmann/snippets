threshold = 10**999

fib = (1,1)
i = 2

while True:
    if fib[0] >= threshold:
        print(i)
        break
    i += 1
    fib = fib[0]+fib[1], fib[0]
