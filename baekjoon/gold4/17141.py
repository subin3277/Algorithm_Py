# 연구소2
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
loca = []
virus = deque()
for i in range(N):
    lst = list(map(int, input().split()))
    loca.append(lst)
    for j in range(N):
        if lst[j] == 2:
            virus.append([i, j, 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []
cnt = 0
for c in combinations(virus, M): # 모든 바이러스를 놓을 수 있는 조합
    time = 0
    tmp = deepcopy(loca) # 위치 초기화
    for i in virus: # 바이러스가 놓인 곳이 아니면
        if not (i in c):
            tmp[i[0]][i[1]] = 0 # 빈 곳으로 처리
    c = list(c)
    while c: # 상하좌우 퍼트리기
        t = c.pop(0)
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if 0 <= x < N and 0 <= y < N and tmp[x][y] == 0:
                c.append([x, y, t[2] + 1])
                tmp[x][y] = 2 # 바이러스 있다고 표시
    time = t[2]
    for i in tmp:
        if 0 in i: # 바이러스가 퍼지지 못하는 곳이 있으면
            time = -1 # 결과 -1
            break
    else:
        res.append(time)
if len(res) == 0:
    print(-1)
else:
    print(min(res)) # 결과중 가장 최소값 출력
