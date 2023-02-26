# 나누기

N = int(input())
F = int(input())

if N % F != 0 :
    n = N // 100 * 100
    for i in range(100):
        if (n+i) % F == 0 :
            ans = str(n + i)
            break
else :
    ans = str(N)
print(ans[-2:])