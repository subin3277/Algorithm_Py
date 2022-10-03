# 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in range(N - 1):
    num[i+1] += num[i]
num = [0] + num
for _ in range(M):
    i, j = map(int, input().split())
    print(num[j] - num[i-1])