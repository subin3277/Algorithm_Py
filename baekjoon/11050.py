N, K = map(int,input().split())

def factorial(N) :
    sum = 1
    for i in range(1,N+1) :
        sum *= i
    return sum

res = factorial(N)/(factorial(K)*factorial(N-K))
print(int(res))