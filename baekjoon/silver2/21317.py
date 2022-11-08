# 징검다리 건너기

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
res = [[0, False] for _ in range(N)]  #[최소 에너지, 큰 점프 여부]
for i in range(1, N):
    if i >= 3 and not res[i-3][1]:
        if res[i-1][0]+lst[i-1][0] > res[i-3][0]+K and res[i - 2][0] + lst[i - 2][1] > res[i-3][0]+K:
            res[i][1] = True
        res[i][0] = min(res[i - 1][0] + lst[i - 1][0], res[i - 2][0] + lst[i - 2][1], res[i - 3][0] + K)
    elif (i >= 3 and res[i-3][1]) or i == 2:
        res[i][0] = min(res[i - 1][0] + lst[i - 1][0], res[i - 2][0] + lst[i - 2][1])
    else:
        res[i][0] = res[i-1][0] + lst[i-1][0]

print(res[-1][0])