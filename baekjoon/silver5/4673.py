# 셀프 넘버

lst = [i for i in range(1, 10001)]

def selfnum(N):
    sum = N
    while N != 0:
        sum += N % 10
        N //= 10
    if sum < 10001:
        if sum in lst:
            lst[lst.index(sum)] = 0
            selfnum(sum)
        else:
            return
    else :
        return

for i in lst:
    if i != 0:
        selfnum(i)
for i in lst:
    if i != 0:
        print(i) 
