# 도로와 신호등
import sys
sys.stdin = open("input.txt", "r")

N, L = map(int, input().split())
light = []
# True = 빨간불, False = 초록불
for i in range(N):
    D, R, G = map(int, input().split())

# 해결xxxxxxxxxxxxxxxxxxxxxxxx 다시해보자^^