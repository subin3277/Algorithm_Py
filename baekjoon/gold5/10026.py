# 적록색약

import sys
sys.setrecursionlimit(1000000)

def dfs(v, w):
    for i in range(4):
        x = v + dx[i]
        y = w + dy[i]
        if 0 <= x < N and 0 <= y < N and not visited[x][y]:
            if color[x][y] == color[v][w]:
                visited[x][y] = True
                dfs(x, y)
N = int(input())
color = [list(map(str, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

yes = no = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            no += 1

for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            yes += 1

print(no, yes)