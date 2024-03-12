# Game Addiction
from collections import deque

H, N = map(int, input().split())
W = abs(H - N) + 1
visit = [[False] * W for _ in range(W)]
ans = [[1] * W for _ in range(W)]

dx = [1, 0]
dy = [0, 1]
ans[0][0] = 1

for i in range(W) :
    for j in range(W) :
        if j > i :
            visit[i][j] = True
            ans[i][j] = 0

queue = deque()
queue.append([0, 0])
while queue :
    x, y = queue.popleft()
    if 0 <= x - 1 and 0 <= y-1 : 
        ans[x][y] = ans[x-1][y] + ans[x][y-1]
    elif 0 <= y - 1 : 
        ans[x][y] = ans[x][y-1]
    elif 0 <= x - 1 : 
        ans[x][y] = ans[x-1][y]

    for i in range(2) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < W and not visit[nx][ny] and nx>=ny :
            queue.append([nx, ny])
            visit[nx][ny] = True

print(ans[-1][-1])