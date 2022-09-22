# 미생물 격리
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N, M, K = map(int, input().split())
    virus = [[0] * N for _ in range(N)]
    loca = [[0] * N for _ in range(N)]
    for i in range(K):
        x, y, c, l = map(int, input().split())
        virus[x][y] = c
        loca[x][y] = l
    # 상-1 하-2 좌-3 우-4
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(M):
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if virus[i][j] != 0:
                    x = i + dx[loca[x][y] - 1]
                    y = j + dy[loca[x][y] - 1]
                    if virus[x][y] != 0:
                        pass

# 해결xxxxxxxxxxxxxxxxxxxxxxxx