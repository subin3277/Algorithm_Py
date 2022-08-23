# 미로
import sys
sys.stdin = open("input.txt", "r")

def findmiro(starti, startj):
    stack = []
    visited = [[False] * N for _ in range(N)]

    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    res = False
    while True:
        for i in range(4): # 상하좌우 하나씩 해보기
            if not (0 <= starti + dx[i] < N and 0 <= startj + dy[i] < N): # 범위에서 벗어나지않도록
                continue
            w = miro[starti + dx[i]][startj + dy[i]]
            if w == 3: # 값이 3이라면 도착점 도달
                res = True
                return res

            if not visited[starti + dx[i]][startj + dy[i]] and miro[starti + dx[i]][startj + dy[i]] == 0:
                stack.append((starti, startj)) # 튜플로 저장
                starti += dx[i]
                startj += dy[i]
                visited[starti][startj] = True
                break
        else:
            if stack: # 스택이 비어있지 않다면
                tmp = stack.pop()
                starti = tmp[0]
                startj = tmp[1]
            else: # 비어있으면
                break
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
                stri = i
                strj = j

    res = findmiro(stri, strj)
    if res:
        print(f'#{test}', 1)
    else:
        print(f'#{test}', 0)