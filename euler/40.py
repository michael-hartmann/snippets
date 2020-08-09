class Problem40:
    def __init__(self, maximum):
        self.s = ""

        for i in range(1,maximum+1):
            self.s += str(i)
            if len(self.s) > maximum:
                break

    def getdigit(self, n):
        return int(self.s[n-1])


problem = Problem40(1000000)

prod = 1
for i in range(0, 6+1):
    n = 10**i
    prod *= problem.getdigit(n)

print(prod)
