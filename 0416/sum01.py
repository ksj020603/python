num = int(input("정수 입력"))
sum = 0
for i in range(0, (num+1),2):
    if (i < num):
            print(i, "+", end="")
    else:
            print(i, "=", end="")
    sum+= i

print(sum)
