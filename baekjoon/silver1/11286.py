# 절댓값 힙

import sys, heapq
input = sys.stdin.readline

heap = []
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
A, B = min(lst), max(lst)
cnt = [0] * ((max(A*(-1), B))+1)

for x in lst:
    if x == 0:
        if heap:
            t = heapq.heappop(heap)
            if cnt[t] > 0:
                cnt[t] -= 1
                print((-1) * t)
            else:
                print(t)
        else:
            print(0)
    else:
        if x < 0:
            cnt[x*(-1)] += 1
            heapq.heappush(heap, x*(-1))
        else:
            heapq.heappush(heap, x)