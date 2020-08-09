def wordcount(word):
    return sum(map(lambda x: ord(x)-64, word))

def slurp(filename):
    with open(filename) as f:
        content = f.readline().replace("\"", "")
    return content.split(",")


if __name__ == "__main__":
    triangle_numbers = set((n*(n+1)//2 for n in range(1,1000)))

    n = 0
    words = slurp("p042_words.txt")
    for word in words:
        if wordcount(word) in triangle_numbers:
            n += 1

    print(n)
