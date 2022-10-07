# 계단 오르기

N = int(input())
stair = [0] * 301
for i in range(N):
    stair[i] = int(input())
res = [0] * 301
res[0] = stair[0]
res[1] = stair[0] + stair[1]
res[2] = max(stair[1] + stair[2], stair[0]+ stair[2])
for i in range(3, N):
    res[i] = max(res[i - 3] + stair[i - 1] + stair[i], res[i - 2] + stair[i])
print(res[N - 1])