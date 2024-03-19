# 점프
N = int(input())
jump = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N) :
    for j in range(N) :
        t = jump[i][j]
        if t == 0 :
            break
        if j + t < N :
            dp[i][j+t] += dp[i][j]
        
        if i + t < N :
            dp[i + t][j] += dp[i][j]

print(dp[-1][-1])