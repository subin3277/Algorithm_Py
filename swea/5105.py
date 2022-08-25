# 미로의 거리
import sys
sys.stdin = open("input.txt", "r")

def bfs(SP, N):
    visited = [[False] * N for _ in range(N)]
    queue = []
    stri = SP[0]
    strj = SP[1]
    queue.append([stri, strj, -1])
    visited[stri][strj] = True

    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]

    while queue:
        t = queue.pop(0)
        stri = t[0]
        strj = t[1]
        if miro[t[0]][t[1]] == 3: # 도착점 만나면 리턴
            return t[2]
        for i in range(4): # 상하좌우
            if 0 <= stri + dx[i] < N and 0 <= strj + dy[i] < N: # 범위 벗어나지 않도록
                if not visited[stri+dx[i]][strj+dy[i]] and miro[stri+dx[i]][strj+dy[i]] != 1:
                    visited[stri+dx[i]][strj+dy[i]] = True # 방문표시
                    queue.append([stri+dx[i], strj+dy[i], t[2] + 1]) # 회수 1증가 후 추가
    return 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    miro = []
    for i in range(N):
        miro.append(list(map(int, input())))

    for i in range(N): # 출발점 찾기
        for j in range(N):
            if miro[i][j] == 2:
                starti = i
                startj = j
                break
    res = bfs([starti, startj], N)
    print(f'#{test} {res}')
