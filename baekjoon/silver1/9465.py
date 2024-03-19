# 스티커

T = int(input())
for _ in range(T) :
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    for i in range(1, N) :
        if i == 1:
            dp[0][i] = dp[1][i-1] + sticker[0][i]
            dp[1][i] = dp[0][i-1] + sticker[1][i]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

    print(max(dp[0][-1], dp[1][-1]))