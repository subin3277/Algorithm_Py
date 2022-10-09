# 경로 찾기

N = int(input())
node = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            node[i].append(j)

ans = [[0] * N for _ in range(N)]

visited = [[False] * N for _ in range(N)]

for i in range(N):
    visited[i][i] = True
    stack = [i]
    while stack:
        t = stack.pop(0)
        for k in node[t]:
            if ans[i][k] == 0:
                ans[i][k] = 1
                stack.append(k)

for i in ans:
    print(*i)
