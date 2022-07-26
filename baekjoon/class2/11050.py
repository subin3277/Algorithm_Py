from functools import lru_cache

N, K = map(int,input().split())

@lru_cache
def factorial(N) :
    sum = 1
    for i in range(1,N+1) :
        sum *= i
    return sum

print(factorial(N),factorial(K))
res = factorial(N)/(factorial(K)*factorial(N-K))
print(int(res))