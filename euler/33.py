from fractions import Fraction

f = Fraction(1,1)

for denominator in range(10,100):
    for numerator in range(10,denominator):
        if numerator % 10 == 0 and denominator % 10 == 0:
            continue

        str_numerator = str(numerator)
        str_denominator = str(denominator)

        num = 0
        denom = 0
        for p,q in ((0,0), (0,1), (1,0), (1,1)):
            if str_numerator[p] == str_denominator[q]:
                num = int(str_numerator[1-p])
                denom = int(str_denominator[1-q])

        if denom == 0:
            continue

        if Fraction(num,denom) == Fraction(numerator,denominator):
            print("%d/%d = %d/%d" % (numerator, denominator, num, denom))
            f *= Fraction(num,denom)

print(f)
