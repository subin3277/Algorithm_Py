# 최소 힙
import heapq, sys

input = sys.stdin.readline
N = int(input())
Q = []
res = []
for i in range(N):
    x = int(input())
    if x == 0:
        if Q:
            res.append(heapq.heappop(Q))
        else:
            res.append(0)
    else:
        heapq.heappush(Q, x)
for i in res:
    print(i)