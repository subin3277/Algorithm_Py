# 미로_bfs
import sys
sys.stdin = open("input.txt", "r")

def bfs(G, stri, strj):
    visited = [[False] * N for _ in range(N)]
    queue = []
    res = False
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    queue.append((stri, strj))
    visited[stri][strj] = True
    while queue:
        t = queue.pop(0)
        stri = t[0]
        strj = t[1]
        if G[t[0]][t[1]] == 3: # 3이면 도착지 찾음
            res = True
            break

        for i in range(4): # 상하좌우 탐색
            if not (0 <= stri + dx[i] < N and 0 <= strj + dy[i] < N):
                continue
            if not visited[stri + dx[i]][strj + dy[i]] and (G[stri + dx[i]][strj + dy[i]] == 0 or G[stri + dx[i]][strj + dy[i]] == 3):
                queue.append((stri + dx[i], strj + dy[i]))
                visited[stri + dx[i]][strj + dy[i]] = True
    return res

T = int(input())
for test in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        tmp = list(map(int, input()))
        miro.append(tmp)
    # 출발점 위치 찾기
    starti = startj = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                starti = i
                startj = j
                break
    res = bfs(miro, starti, startj)
    if res:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')