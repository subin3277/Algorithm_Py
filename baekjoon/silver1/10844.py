# 쉬운 계단 수

N = int(input())
ans = 0
lst = [0]+[1]*9
tmp = [0]*10

for i in range(1,N):
    tmp = [0]*10
    for j in range(len(lst)):
        if j == 0:
            tmp[j+1] += lst[j]
        elif j == 9:
            tmp[j-1] += lst[j]
        else:
            tmp[j-1] += lst[j]
            tmp[j+1] += lst[j]
    for j in range(len(lst)):
        lst[j] = tmp[j]%1000000000
print(sum(lst)%1000000000)