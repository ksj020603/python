score = [70, 60, 55, 75, 95, 90, 80, 85, 100]

hap = 0

for i in score:
    hap = hap + i

print("평균 = %.10000f" % (hap/len(score)))
