# 도넛 행성
from collections import deque

N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
for i in range(N) :
    for j in range(M) :
        if planet[i][j] == 0 and not visited[i][j] :
            visited[i][j] = True
            queue = deque()
            queue.append((i, j))
            while queue :
                ti, tj = queue.popleft()
                for k in range(4) :
                    nx = ( ti + dx[k] ) % N
                    ny = ( tj + dy[k] ) % M
                    if 0 <= nx < N and 0 <= ny < M and planet[nx][ny] == 0 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            answer += 1

print(answer)