a = 3; b = ~a;
print("a=",a,"b=",b)

a = 3; b = 5;
c = a & b # AND 둘 중에 하나라도 0이면 0(둘 다 1이면 1)
print("a=",a,"b=",b,"c=",c)

a = 3; b = 5;
c = a ^ b
print("a=",a,"b=",b,"c=",c) # exclusive OR 2개가 같으면 0 다르면 1

a = 3; b = 5;
c = a | b # OR 두 개 중에 하나라도 1이라면 1(둘 다 0 이면 0)
print("a=",a,"b=",b,"c=",c)
