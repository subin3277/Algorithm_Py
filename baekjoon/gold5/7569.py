# 토마토
from collections import deque
M, N, H = map(int, input().split())
tomato = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    tomato.append(tmp)

dx = [0,0,-1,1,0,0] # 상하좌우위아래
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]
queue = deque()
count0 = 0
for i in range(H): # 익은 토마토 위치 저장
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k, 0])

day = -1
while queue: # 익힐 수 있는 토마토가 없을 때까지
    t = queue.popleft()
    day = t[3]
    for i in range(6):
        z = t[0] + dz[i]
        y = t[1] + dy[i]
        x = t[2] + dx[i]
        if 0 <= x < M and 0 <= y < N and 0 <= z < H and tomato[z][y][x] == 0:
            tomato[z][y][x] = 1 # 토마토 익히기
            queue.append([z, y, x, t[3]+1]) # 좌표와 몇번째날인지 저장

for i in tomato:
    for j in i:
        if 0 in j: # 못익힌 토마토가 있다면
            day = -1 # -1 출력
            break
    if day == -1:
        break
print(day)