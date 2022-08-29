# 재미있는 오셀로 게임
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[-1] * N for _ in range(N)]
    board[N//2][N//2] = board[N//2 - 1][N // 2 - 1] = 1 # 2 백돌
    board[N//2][N//2 - 1] = board[N // 2 - 1][N // 2] = 0 # 1 흑돌
    dx = [-1, 1, 0, 0, 1, 1, -1, -1] # 상하좌우
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    for i in range(M):
        x, y, rock = map(int, input().split())
        board[y - 1][x - 1] = rock - 1
        stack = [(y-1, x-1)]
        for j in range(8):
            nxtx = y - 1 + dx[j]
            nxty = x - 1 + dy[j]
            if 0 <= nxtx < N and 0 <= nxty < N: # 칸 밖으로 나가는지 판별
                if board[nxtx][nxty] == 2 - rock:
                    stack.append((nxtx, nxty)) # 스택에 추가
                    res = True
                    while 0 <= nxtx < N and 0 <= nxty < N and board[nxtx][nxty] != rock - 1: # 옆에 다른 돌이 있는지 확인
                        nxtx += dx[j]
                        nxty += dy[j]
                        stack.append((nxtx, nxty)) # 스택에 추가
                        if not (0 <= nxtx < N and 0 <= nxty < N) or board[nxtx][nxty] == -1: # -1을 만나면 중단
                            res = False
                            stack = [(y-1, x-1)]
                            break
                    while res and stack: # 지나온 길동안
                        t = stack.pop()
                        board[t[0]][t[1]] = rock - 1 # 값 바꾸기

    w = b = 0
    for i in board:
        w += i.count(1)
        b += i.count(0)
    print(f'#{test} {b} {w}')
