# 자리 배정
import sys
sys.stdin = open("input.txt", "r")

C, R = map(int, input().split())
K = int(input())
seat = [[0]*C for _ in range(R)]

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]
if K <= C*R: # 최대 인원수를 넘으면
    i = R - 1
    j = 0
    k = 0
    for num in range(1, K+1):
        seat[i][j] = num
        if num == K:
            break
        if not (0 <= i+dx[k] < R) or not (0 <= j+dy[k] < C) or seat[i+dx[k]][j+dy[k]] != 0: # 범위안에 있지 않거나 이미 입력된 곳이라면
            if k == 3: # 방향 바꾸기
                k = 0
            else:
                k += 1
        i += dx[k] # i, j 이동
        j += dy[k]
    print(j + 1, R - i)
else:
    print(0) # 0 프린트