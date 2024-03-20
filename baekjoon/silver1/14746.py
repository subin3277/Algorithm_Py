# 현수막
from collections import deque

M, N = map(int, input().split())
letter = [list(map(int, input().split())) for _ in range(M)]
visit = [[False] * N for _ in range(M)]
ans = 0

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
for i in range(M) :
    for j in range(N) :
        if visit[i][j] :
            continue
        if letter[i][j] == 0 :
            visit[i][j] = True
            continue
        
        ans += 1
        queue = deque()
        queue.append([i, j])
        while queue :
            x, y = queue.popleft()
            for k in range(8) :
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and not visit[nx][ny] and letter[nx][ny] == 1:
                    visit[nx][ny] = True
                    queue.append([nx, ny])
print(ans)
