# 가장 긴 감소하는 부분 수열

N = int(input())
num = list(map(int, input().split()))

dp = [1 for _ in range(N)]
for i in range(N) :
    for j in range(i) :
        if num[i] < num[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))