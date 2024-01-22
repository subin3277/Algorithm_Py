# 포도주 시식
N = int(input())
num = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 2)
cnt = 0
dp[1] = num[1]
if N > 1:
    dp[2] = num[1] + num[2]
for i in range(3, N+1) :
    dp[i] = max(dp[i-3] + num[i-1] + num[i], dp[i-2] + num[i], dp[i-1])
print(dp[N])