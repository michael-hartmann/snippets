def slurp():
    with open("p022_names.txt") as f:
        s = f.readline()
    s = s.replace("\"", "")
    return sorted(s.split(","))

def namecount(name):
    return sum(map(lambda c: ord(c)-64, name))

if __name__ == "__main__":
    names = slurp()

    total = 0
    for i, name in enumerate(names):
        pos = i+1
        total += pos*namecount(name)

    print(total)
