# 정사각형 방
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    room = []
    for i in range(N):
        room.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(N)]
    res = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    maxnum = 1000000
    maxcnt = 0
    for i in range(N):
        for j in range(N):
            stack = [[i, j, 1]]
            state = False
            visited[i][j] = True
            while stack:
                t = stack.pop(0)
                for k in range(4):
                    x = t[0] + dx[k]
                    y = t[1] + dy[k]
                    if 0 <= x < N and 0 <= y < N and room[t[0]][t[1]] + 1 == room[x][y]:
                        if not visited[x][y]:
                            stack.append([x, y, t[2] + 1])
                            visited[x][y] = True
                        else:
                            res[i][j][0] = room[i][j]
                            res[i][j][1] = t[2] + res[x][y][1]
                            state = True
                            break
                if state:
                    break
            if not state:
                res[i][j][0] = room[i][j]
                res[i][j][1] = t[2]

    for i in range(N):
        for j in range(N):
            if maxcnt < res[i][j][1]:
                maxcnt = res[i][j][1]
                maxnum = res[i][j][0]
            elif maxcnt == res[i][j][1]:
                if maxnum > res[i][j][0]:
                    maxcnt = res[i][j][1]
                    maxnum = res[i][j][0]
    print(f'#{test} {maxnum} {maxcnt}')