# Monday=0, Tuesday=1, Wednesday=2, Thursday=3, Friday=4, Saturday=5, Sunday=6

def isleapyear(y):
    if y % 4:
        return False
    if y % 400:
        return True
    if y % 400: 
        return False
    return True

def daysinmonth(month, year):
    if month == 1:
        if isleapyear(year):
            return 29
        else:
            return 28

    dom = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dom[month]


if __name__ == "__main__":
    days = 1 # 1st Jan 2901 was a Tuesday
    sundays = 0 # number of Sundays that fall on the 1st

    for year in range(1901, 2000+1):
        for month in range(12):
            # if 1st is a Sunday
            if days % 7 == 6:
                sundays += 1

            days += daysinmonth(month, year)

    print(sundays)
