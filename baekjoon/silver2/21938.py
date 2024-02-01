# 영상처리
from collections import deque

N, M = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

display = [[0] * M for _ in range(N)]
for i in range(N) :
    for j in range(0, M * 3, 3) :
        aver = sum(color[i][j : j+3]) / 3
        if aver >= T :
            display[i][j // 3] = 255
        else :
            display[i][j // 3] = 0

answer = 0 
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([])

for i in range(N) :
    for j in range(M) :
        if not visited[i][j] :
            visited[i][j] = True
            if display[i][j] == 255 :
                answer += 1
                queue = deque([(i, j)])

        while queue :
            x, y = map(int, queue.popleft())
            for t in range(4) :
                nx = x + dx[t]
                ny = y + dy[t]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                    visited[nx][ny] = True
                    if display[nx][ny] == 255 :
                        queue.append((nx, ny))
        
print(answer)