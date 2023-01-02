# 셀프 넘버

def selfnum(N):
    sum = N
    while N != 0:
        sum += N % 10
        N //= 10
    return sum

for i in range(100):
    if selfnum(i) != i :
        print(i)
