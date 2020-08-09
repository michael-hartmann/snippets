from math import log

maximum = (0, -1)

with open("p099_base_exp.txt") as f:
    for i,line in enumerate(f):
        b,e = map(int, line.split(","))

        log_value = e*log(b)
        if log_value > maximum[0]:
            linenumber = i+1
            maximum = (log_value, linenumber)

    print(maximum)
