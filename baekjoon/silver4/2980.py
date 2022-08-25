# 도로와 신호등
import sys
sys.stdin = open("input.txt", "r")

N, L = map(int, input().split())
light = []
# True = 빨간불, False = 초록불
traffic = [[True] * (L+1) for _ in range(N)]
for i in range(N):
    D, R, G = map(int, input().split())
    k = 1
    res = True
    while True:
        for j in range(G):
            if k * R + j <= L:
                traffic[i][k * R + j] = False
            else:
                res = False
                break
        else: k += 1
        if not res:
            break
print(traffic)
truck = 1
second = 1
lightidx = 0
while truck <= L:
    if lightidx == N:
        while truck <= L:
            second += 1
            truck += 1
        break

    for i in range(N):
        if second % (light[i][1] + light[i][2]) == light[i][2] or second % (light[i][1] + light[i][2]) == 0:
            light[i][3] = not light[i][3]

    if truck == light[lightidx][0]:
        if not light[lightidx][3]:
            lightidx += 1
        else:
            truck -= 1
    second += 1
    truck += 1
print(second-1)

# 해결xxxxxxxxxxxxxxxxxxxxxxxx