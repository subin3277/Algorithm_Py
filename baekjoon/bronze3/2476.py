# 주사위 게임

N = int(input())
ans = 0
for _ in range(N):
    A, B, C= map(int, input().split())
    if A == B == C:
        res = 10000 + A * 1000
    elif A==B:
        res = 1000 + A * 100
    elif B == C :
        res = 1000 + B * 100
    elif C == A :
        res = 1000 + C * 100
    else:
        res = max(A, B, C) * 100
    ans = max(ans, res)
print(ans)