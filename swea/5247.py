# 연산
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())

    res = 0
    dist = [0] * 1000001
    queue = deque()
    queue.append(N)
    while queue:
        t = queue.popleft()
        if t == M:
            res = dist[t]
            break
        for i in (t+1, t-1, t*2, t-10):
            if 0 <= i <= 1000000 and not dist[i]:
                dist[i] = dist[t] + 1
                queue.append(i)

    print(f'#{test} {res}')