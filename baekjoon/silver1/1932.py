# 정수 삼각형

N = int(input())
triangle = []
dp = []
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    triangle.append(tmp)
    dp.append([0] * i)

dp[0][0] = triangle[0][0]
for i in range(1, N):
    left = right = 0
    for j in range(len(triangle[i])):
        if j != 0 and j != len(triangle[i]) - 1:
            left = right
            right = dp[i-1][j]
        elif j == 0:
            left = 0
            right = dp[i-1][0]
        else:
            left = dp[i-1][-1]
            right = 0
        dp[i][j] = max(left, right) + triangle[i][j]
print(max(dp[-1]))