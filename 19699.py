# 소-난다!
import math

N, M = map(int,input().split())
cow = list(map(int, input().split()))
cow.sort()

n = sum(cow)
prime = [True for _ in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] :
        j = 2
        while i * j <= n:
            prime[i*j] = False
            j += 1

answer = set()
def combination(sum, idx, cnt) :
    global answer
    if cnt == M:
        if prime[sum] :
            answer.add(sum)
        return
    nx = idx + 1
    if nx < len(cow) :
        combination(sum + cow[nx], nx, cnt + 1)
        combination(sum, nx, cnt)
    else:
        return
combination(0, -1, 0)
if len(answer) > 0 :
    ans = sorted(list(answer))
else:
    ans = [-1]
print(*ans)