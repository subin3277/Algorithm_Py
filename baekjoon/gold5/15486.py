# 퇴사2

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
for i in range(N) :
    t, p = schedule[i][0], schedule[i][1]
    dp[i] = max(dp[i], dp[i-1])

    if i+t <= N:
        dp[i+t] = max(dp[i+t], dp[i]+p )

print(max(dp))