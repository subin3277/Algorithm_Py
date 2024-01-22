# 연속합
N = int(input())
num = list(map(int, input().split()))
dp = [0] * len(num)
for i in range(len(num)) :
    if i == 0 :
        dp[i] = num[i]
    else:
        dp[i] = max(dp[i-1] + num[i], num[i])
print(max(dp))