total = 0

for p200 in (0,1):
    for p100 in (0,1,2):
        for p50 in (0,1,2,3,4):
            for p20 in range(10+1):
                for p10 in range(20+1):
                    for p5 in range(40+1):
                        for p2 in range(100+1):
                            s = p200*200+p100*100+p50*50+p20*20+p10*10+p5*5+p2*2

                            if s <= 200:
                                total += 1

print(total)
