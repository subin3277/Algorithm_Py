# 양치기 꿍
from collections import deque
R, C = map(int, input().split())
ground = [list(map(str, input())) for _ in range(R)]

# # : 울타리 / v : 늑대 / k : 양 / . : 빈공간
visited = [[False] * C for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer_wolf = 0
answer_sheep = 0

for i in range(R) :
    for j in range(C) :
        if not visited[i][j] :
            visited[i][j] = True
            queue = deque([])
            queue.append([i, j])
            wolf = 0
            sheep = 0
            while queue :
                tx, ty = queue.popleft()
                if ground[tx][ty] == 'v' :
                    wolf += 1
                elif ground[tx][ty] == 'k' :
                    sheep += 1
                elif ground[tx][ty] == '#' :
                    continue
                for t in range(4) :
                    vx = tx + dx[t]
                    vy = ty + dy[t]
                    if 0 <= vx < R and 0 <= vy < C and not visited[vx][vy] :
                        visited[vx][vy] = True
                        if ground[tx][ty] != '#':
                            queue.append([vx, vy])
            if wolf >= sheep:
                answer_wolf += wolf
            else :
                answer_sheep += sheep
print(answer_sheep, answer_wolf)