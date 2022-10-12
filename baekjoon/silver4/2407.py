# 조합

def factorial(N):
    if N == 1:
        return N
    return N * factorial(N-1)

n, m = map(int, input().split())
tmp = 1
for i in range(n, max(m, n-m), -1):
    tmp *= i
res = tmp // factorial(min(m,n-m))
print(res)