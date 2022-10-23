# 숨바꼭질 3
from collections import deque

N, K = map(int, input().split())

stack = deque()
stack.append([N, 0])
tmp = 100000
visited = [False] * (tmp+1)
visited[N] = True
while stack:
    t, s = stack.popleft()
    if t == K:
        print(s)
        break
    if 0< t*2 < tmp+1 and not visited[t*2]:
        stack.appendleft([t*2,s])
        visited[t*2] = True
    if 1 <= t < tmp+1 and not visited[t-1]:
        stack.append([t-1, s+1])
        visited[t-1] = True
    if -1 <= t < tmp-1 and not visited[t+1]:
        stack.append([t+1, s+1])
        visited[t+1] = True