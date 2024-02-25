# 캠프 준비

N, L, R, X = map(int, input().split())
problem = list(map(int, input().split()))
problem.sort()
ans = 0

def BT(idx, res, sum):
    global ans
    if sum > R :
        return
    
    if L <= sum <= R and len(res) >= 2 and max(res) - min(res) >= X :
        ans += 1
    
    for i in range(idx, N) :
        BT(i+1, [*res, problem[i]], sum+problem[i])

BT(0, [], 0)
print(ans)