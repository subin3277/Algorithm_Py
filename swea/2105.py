# 디저트 카페
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    cafe = []
    for _ in range(N):
        cafe.append(list(map(int, input().split())))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, N-1):
        for j in range(1, N-1):
            pass

# 해결 xxxxxxxxxxxxxxxx