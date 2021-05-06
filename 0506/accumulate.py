'''
hap = 0
i = 1
while i <= 100:
        hap = hap + i
        i = i + 1

print("합 = %d" % hap)
''' '''
everHap = 0
oddHap = 0
i = 1
while i <= 100:
    if i % 2 == 0 :
        everHap = everHap + i
    else:
       oddHap = oddHap + i
        i = i + 1
''' '''
sevenHap = 0
i = 1
while i <= 100:
    if i % 7 == 0 :
        sevenHap = sevenHap + i
        i = i + 1

print("1~100 7의 배수 합 = %d %sevenHap)
''' '''
hap = 0
i = 1
while i <= 100:
    hap = hap + i
    if hap >= 1000 :
        break
    i = i + 1

print("1~100 합 중에 처음으로 1000을 넘는 수 %d와 %d 까지의 합 = %d" % (i, hap))
''' '''
hap = 0
i = 0
while i <= 100:
    i = i + 1
    if i % 7 == 0:
        continue
    hap = hap + i

print("1~100 합 중에 7의 배수를 제외한 나머지 합 = %d" % hap)
'''


