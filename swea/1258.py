# 행렬 찾기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = []
    size = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    i = j = 0
    while i < N:
        while j < N:
            if matrix[i][j] != 0:
                W = H = k = 0
                while matrix[i][j+k] != 0:
                    W += 1
                    k += 1
                k = 0
                while matrix[i+k][j] != 0:
                    H += 1
                    k += 1
                j += W
                i += H
                size.append([W, H])
            j += 1
        i += 1
    print(size)

# 해결xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx