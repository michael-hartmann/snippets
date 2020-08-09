def number2word(n):
    if n < 20:
        d = (
            "zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        )
        return d[n]

    if n < 100:
        d = (
            False, False, "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"
        )

        if n % 10 == 0:
            return d[n//10]
        else:
            return d[n//10] + "-" + number2word(n % 10)

    if n < 1000:
        hundreds = n // 100
        if n % 100:
            return number2word(hundreds) + " hundred and " + number2word(n%100)
        else:
            return number2word(hundreds) + " hundred"

    
    if n == 1000:
        return "one thousand"

def count(s):
    return len(s.replace(" ", "").replace("-", ""))

if __name__ == "__main__":
    s = 0
    for i in range(1,1001):
        print(i, number2word(i), count(number2word(i)))
        s += count(number2word(i))

    print(s)
