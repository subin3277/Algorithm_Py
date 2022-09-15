# 연구소2
from collections import deque
from itertools import combinations

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
for c in combinations(virus, M):
    time = 0
    tmp = loca.copy()
    for i in virus:
        if not i in c:
            tmp[i[0]][i[1]] = 0
    c = list(c)
    while c:
        t = c.pop(0)
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if 0 <= x < N and 0 <= y < N and tmp[x][y] == 0:
                c.append([x, y, t[2] + 1])
                tmp[x][y] = 2
    time = t[2] + 1
    for i in tmp:
        if 0 in i:
            time = -1
            break
    res.append(time)
print(res)
if res.count(-1) == len(res):
    print(-1)
else:
    for i in res:
        pass
    print(min(res))

# 해결xxxxxxxxxxxxxxxxxxxxxxxx