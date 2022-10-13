# 아기 상어
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def move(x1, y1): # 최소 거리로 갈 수 있는 곳 찾기
    global ans
    queue = deque()
    queue.append((x1, y1, 0))
    visited = [[False] * N for _ in range(N)]
    visited[x1][y1] = True
    while queue:
        x, y, k = queue.popleft()
        if (x, y) in fish:
            fish.remove((x, y)) # 먹은 물고기 지우기
            lst[x][y] = 0
            ans += k # 이동거리 더하기
            print(k)
            return x, y # 상어 위치 갱신

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if 0 <= lst[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, k+1))
    return -1, -1

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

x = y = 0
for i in range(N): # 현재 상어 위치
    if 9 in lst[i]:
        x = i
        y = lst[i].index(9)
        lst[x][y] = 0
        break

size = 2 # 상어 크기
eat = 0
sizestate = False # 먹을 수 있는 고기 갯수 세기위한 state
fish = []
ans = 0
while True:
    if size == eat: # 크기만큼 먹으면 사이즈 증가
        size += 1
        eat = 0
        sizestate = False

    if not sizestate: # 사이즈 증가하면 먹어야할 물고기리스트 갱신
        sizestate = True
        fish = []
        for i in range(N):
            for j in range(N):
                if 0 < lst[i][j] < size:
                    fish.append((i, j))

    if len(fish) >= 1:
        x, y = move(x, y)
        if x == -1:
            break
        else:
            eat += 1
    else:
        break

print(ans)