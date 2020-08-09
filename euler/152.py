from fractions import Fraction

goal = Fraction(1,2)-Fraction(1,2*2)

def combinations(fracs):
    l = [0]
    def add(term):
        threshold = goal-term
        l2 = [x+term for x in l if x < threshold]
        l.extend(l2)

    for i,term in enumerate(fracs):
        add(term)

    return l
    

#fracs = [ Fraction(1,i*i) for i in range(3,46)]

fracs1 = [ Fraction(1,i*i) for i in range(3,25)]
fracs2 = [ Fraction(1,i*i) for i in range(26,46)]

# fracs2
l1 = combinations(fracs1)
print(float(min(l1)), float(max(l1)))

l2 = combinations(fracs2)
print(float(min(l2)), float(max(l2)))

print("set2")
set2 = set(l2)


# fracs1
print(float(min(l1)), float(max(l1)))
print("list1")


print("combinations")

total = 0
for elem in l1:
    x = goal-elem
    if x in set2:
        print("found")
        total += 1

print(total)
