# 재미있는 오셀로 게임
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    board = [[-1] * N for _ in range(N)]
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 0
    board[N // 2][N // 2] = board[N // 2 - 1][N // 2 - 1] = 1

    dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우 왼위 오위 왼아 오아
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    # 1은 흑 2는 백 -> 흑은 0 백은 1
    for _ in range(M):
        x, y, c = map(int, input().split())
        color = 1
        if c == 1:
            color = 0
        x -= 1
        y -= 1
        board[x][y] = color

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            stack = [[nx, ny]]
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1 - color:
                nx += dx[i]
                ny += dy[i]
                stack.append([nx, ny])
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                while stack:
                    t = stack.pop()
                    board[t[0]][t[1]] = color

    black = white = 0
    for i in board:
        black += i.count(0)
        white += i.count(1)
    print(f'#{test} {black} {white}')
