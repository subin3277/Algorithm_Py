# 탈주범 검거
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
for test in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([R, C])
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    res = deque()
    for _ in range(L - 1):
        length = len(queue)
        for _ in range(length):
            t = queue.popleft()
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                    # 밑에 if문 수정하기~~~~~~~~~~~~ 상-하 / 좌-우
                    for j in range(len(pipe[under[t[0]][t[1]]])):
                        pass
                    if pipe[under[t[0]][t[1]]][j] == pipe[under[x][y]][j] == 1:
                        queue.append([x, y])
                        visited[x][y] = True
        res += queue
    print(queue)
    print(res)
    print(f'#{test} {len(res) + 1}')