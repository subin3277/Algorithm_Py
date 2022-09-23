# 미생물 격리
import sys
sys.stdin = open("input.txt", "r")
from copy import deepcopy

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
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    for _ in range(M):
        nextvirus = [[0] * N for _ in range(N)]
        nextloca = [[0] * N for _ in range(N)]
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if virus[i][j] != 0:
                    x = i + dx[loca[i][j]]
                    y = j + dy[loca[i][j]]
                    if 0 < x < N-1 and 0 < y < N-1 and not visited[x][y]:
                        nextvirus[x][y] = virus[i][j]
                        nextloca[x][y] = loca[i][j]
                        virus[i][j] = 0
                        loca[i][j] = 0
                        visited[x][y] = True
                    elif 0 < x < N-1 and 0 < y < N-1 and visited[x][y]:
                        tmp = [[x, y, nextvirus[x][y], nextloca[x][y]]]
                        for k in range(1, 5):
                            x1 = x + dx[k]
                            y1 = y + dy[k]
                            if 0 <= x1 < N and 0 <= y1 < N and virus[x1][y1] != 0:
                                if (k == 1 or k == 3) and loca[x1][y1] == k + 1:
                                    tmp.append([x1, y1, virus[x1][y1], loca[x1][y1]])
                                elif (k == 2 or k == 4) and loca[x1][y1] == k - 1:
                                    tmp.append([x1, y1, virus[x1][y1], loca[x1][y1]])

                        tmpsum = 0
                        for k in tmp:
                            tmpsum += k[2]
                            virus[k[0]][k[1]] = 0
                            loca[k[0]][k[1]] = 0
                            if nextvirus[x][y] < k[2]:
                                nextvirus[x][y] = k[2]
                                nextloca[x][y] = k[3]

                        nextvirus[x][y] = tmpsum
                    elif x == 0 or x == N - 1 or y == 0 or y == N-1: #가장자리 갔을 때
                        nextvirus[x][y] = virus[i][j] // 2 # 미생물 수 바꾸기
                        if loca[i][j] == 1 or loca[i][j] == 3: # 방향 바꾸기
                            nextloca[x][y] = loca[i][j] + 1
                        else:
                            nextloca[x][y] = loca[i][j] - 1
        virus = deepcopy(nextvirus)
        loca = deepcopy(nextloca)
        print(virus)
    res = 0
    for i in virus:
        res += sum(i)
    print(f'#{test} {res}')