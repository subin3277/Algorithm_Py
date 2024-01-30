# 쉬운 최단거리
from collections import deque

N, M = map(int, input().split())

route = [list(map(int, input().split())) for _ in range(N)]
answer = [[N*M] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
start = [0, 0]

for i in range(N) :
    if 2 in route[i]:
        start = [i, route[i].index(2)]
        visited[start[0]][start[1]] = True
        answer[start[0]][start[1]] = 0
        break

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([start])

while queue :
    x, y = map(int, queue.popleft())
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and route[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            answer[nx][ny] = min(answer[x][y] + 1, answer[nx][ny])
            queue.append([nx, ny])

for i in range(N):
    tmp = answer[i].copy()
    if N*M in tmp:
        res = [x for x,y in enumerate(tmp) if y == N*M]
        for j in res :
            if route[i][j] == 0 :
                tmp[j] = 0
            else :
                tmp[j] = -1
    print(*tmp)