# 숨바꼭질
from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append(N)
dist = [0] * 100001
while queue:
    t = queue.popleft()
    if t == K:
        print(dist[t])
        break

    for i in (t-1, t+1, t*2):
        if 0 <= i <= 100000 and not dist[i]:
            dist[i] = dist[t] + 1
            queue.append(i)
