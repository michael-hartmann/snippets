def palindrome(s):
    return s == s[::-1]

s = 0
for i in range(1,1000000):
    decimal = str(i)

    if palindrome(decimal):
        binary  = "{0:b}".format(i)
        if palindrome(binary):
            print(decimal, binary)
            s += i


print(s)
