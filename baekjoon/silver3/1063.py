# 킹
import sys
sys.stdin = open("input.txt", "r")

KL, RL, N = map(str, input().split())
nkx = ord(KL[0]) - 64
nky = int(KL[1])
rx = ord(RL[0]) - 64
ry = int(RL[1])
for i in range(int(N)):
    move = input()
    kx = nkx
    ky = nky
    # 입력 값에 따라 위치 옮기기
    if move == 'R':
        nkx = kx + 1
    elif move == 'L':
        nkx = kx - 1
    elif move == 'B':
        nky = ky - 1
    elif move == 'T':
        nky = ky + 1
    elif move == "RT":
        nkx = kx + 1
        nky = ky + 1
    elif move == "LT":
        nkx = kx - 1
        nky = ky + 1
    elif move == "RB":
        nkx = kx + 1
        nky = ky - 1
    elif move == "LB":
        nkx = kx - 1
        nky = ky - 1

    if nkx == rx and nky == ry: # 돌과 위치 같으면 돌도 움직이기
        rx += nkx - kx
        ry += nky - ky
        if not (1 <= rx <= 8 and 1 <= ry <= 8): # 칸 넘어가면 원래대로
            rx -= nkx - kx
            ry -= nky - ky
            nkx = kx
            nky = ky
            continue

    if not (1 <= nkx <= 8 and 1 <= nky <= 8): # 칸 넘어가면 원래대로
        nkx = kx
        nky = ky
        continue

KL = chr(nkx + 64) + str(nky)
RL = chr(rx + 64) + str(ry)
print(KL)
print(RL)
