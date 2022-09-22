# 최소합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    num = []
    for _ in range(N):
        num.append(list(map(int, input().split())))

    dx = [1, 0]
    dy = [0, 1]
    visited = [[False] * N for _ in range(N)]
    lst = [[0] * N for _ in range(N)]
    stack = [(0, 0, num[0][0])]
    visited[0][0] = True
    lst[0][0] = num[0][0]
    state = True
    while stack:
        t = stack.pop(0)
        for i in range(2):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if x < N and y < N and not visited[x][y]:
                visited[x][y] = True
                lst[x][y] = t[2] + num[x][y]
                stack.append((x, y, t[2] + num[x][y]))
            elif x < N and y < N and visited[x][y]:
                stack.remove((x, y, lst[x][y]))
                lst[x][y] = min(t[2] + num[x][y], lst[x][y])
                if x == N-1 and y == N-1:
                    state = False
                    break
                stack.append((x, y, min(t[2] + num[x][y], lst[x][y])))
        if not state:
            break

    print(f'#{test} {lst[N-1][N-1]}')