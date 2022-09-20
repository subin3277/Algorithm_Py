# 토마토
from collections import deque

M, N = map(int, input().split())
box = []
stack = deque()
for i in range(N):
    box.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            stack.append([i, j, 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
while stack:
    t = stack.popleft()
    for i in range(4):
        x = t[0] + dx[i]
        y = t[1] + dy[i]
        if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
            box[x][y] = 1
            stack.append([x, y, t[2] + 1])
            ans = t[2] + 1

for i in box:
    if 0 in i:
        ans = -1
        break
print(ans)
