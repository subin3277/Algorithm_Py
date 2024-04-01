# 침투
from collections import deque

M, N = map(int, input().split())
loca = [list(map(int, input())) for _ in range(M)]
visit = [[False] * N for _ in range(M)]

ans = 'NO'

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N) :
    if visit[0][i] : continue
    queue = deque([])
    queue.append((0, i))

    while queue : 
        x, y = queue.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not visit[nx][ny] :
                visit[nx][ny] = True
                if loca[nx][ny] == 0 :
                    if nx == M-1 :
                        print("YES")
                        exit()
                    queue.append((nx, ny))

print(ans)