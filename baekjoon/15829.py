L = int(input())

r = 31
M = 1234567891
str = input()
sum = 0
for i in range(L) :
    sum += (ord(str[i])-96)*(31**i)%M
res = sum % M
print(res)