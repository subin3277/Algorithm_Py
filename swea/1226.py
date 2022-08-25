# 미로1
import sys
sys.stdin = open("input.txt", "r")

def bfs(stri, strj, N):
    visited = [[False]*N for _ in range(N)]
    queue = []
    queue.append((stri, strj))
    visited[stri][strj] = True

    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    while queue:
        t = queue.pop(0)
        stri = t[0]
        strj = t[1]
        if miro[stri][strj] == 3:
            return 1
        for i in range(4):
            if 0 <= stri + dx[i] < N and 0 <= strj + dy[i] < N:
                if not visited[stri + dx[i]][strj + dy[i]] and miro[stri + dx[i]][strj + dy[i]] != 1:
                    queue.append((stri + dx[i], strj + dy[i]))
                    visited[stri + dx[i]][strj + dy[i]] = True
    return 0

T = 10
for test in range(1, T+1):
    Test = int(input())
    N = 16
    miro = []
    for i in range(N):
        miro.append(list(map(int, input())))
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                starti = i
                startj = j
    res = bfs(starti, startj, N)

    print(f'#{test} {res}')

