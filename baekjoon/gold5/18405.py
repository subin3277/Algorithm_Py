# 경쟁적 전염

from collections import deque
N, K = map(int, input().split())
loca = []
for _ in range(N):
    loca.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

queue = deque()
queue2 = deque() # 바이러스가 이미 있는 곳을 저장할 리스트
for i in range(N):
    for j in range(N):
        if loca[i][j] != 0:
            queue.append([i, j])
            queue2.append([i, j])

for _ in range(S):
    if loca[X-1][Y-1] != 0: # 이미 바이러스가 생겼다면 중단
        break
    queue = queue2.copy()
    virus = [[False] * N for _ in range(N)] # 중복 확인 하기 위한 리스트
    while queue:
        i = queue.popleft()
        for j in range(4): # 상하좌우 확인하기
            x = i[0] + dx[j]
            y = i[1] + dy[j]
            if 0 <= x < N and 0 <= y < N and (loca[x][y] == 0 or virus[x][y]):
                if loca[x][y] == 0: # 바이러스가 없다면
                    loca[x][y] = loca[i[0]][i[1]]
                    virus[x][y] = True
                    queue2.append([x, y])
                else: # 바이러스가 있다면
                    loca[x][y] = min(loca[x][y], loca[i[0]][i[1]]) # 최소값의 바이러스
print(loca[X-1][Y-1])

