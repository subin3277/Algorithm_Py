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
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    for _ in range(M):
        nextvirus = [[0] * N for _ in range(N)]
        nextloca = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmp = []
                for k in range(1, 5):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 < x < N-1 and 0 < y < N-1 and virus[x][y] != 0:
                        if (k == 1 or k == 3) and loca[x][y] == k + 1:
                            tmp.append([x, y, virus[x][y], loca[x][y]])
                        elif (k == 2 or k == 4) and loca[x][y] == k - 1:
                            tmp.append([x, y, virus[x][y], loca[x][y]])
                    elif x == 0 or x == N - 1 or y == 0 or y == N - 1:
                        if k == 1 or k == 3:
                            loca[x][y] += 1
                        elif k == 2 or k == 4:
                            loca[x][y] -= 1
                        tmp.append([x, y, virus[x][y]//2, loca[x][y]])
                maxres = 0
                maxloca = 0
                tmpsum = 0
                for h in tmp:
                    tmpsum += h[2]
                    if maxres < h[2]:
                        maxres = h[2]
                        maxloca = h[3]
                nextvirus[i][j] = tmpsum
                nextloca[i][j] = maxloca
    ans = 0
    for i in virus:
        ans += sum(i)
    print(f'#{test} {ans}')

    # 해결xxxxxxxxxxxxxxxxx
