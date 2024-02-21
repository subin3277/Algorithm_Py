# 징검다리 건너기
N = int(input())
num = [[0,0]] +[list(map(int, input().split())) for _ in range(N-1)]
K = int(input())

dp = [0] * (N+1)
dp[2] = num[1][0]
dp[3] = min(num[1][0] + num[2][0], num[1][1])
for i in range(4, N+1) :
    dp[i] = min(dp[i-1] + num[i-1][0], dp[i-2] + num[i-2][1])
print(dp)

# for x in range(1, N-2) :
#     dp2 = dp.copy()
    