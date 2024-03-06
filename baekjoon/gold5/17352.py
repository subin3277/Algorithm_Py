# 여러분의 다리가 되어 드리겠습니다!
from collections import deque

N = int(input())
bridge = [[] for _ in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    bridge[a].append(b)
    bridge[b].append(a)

visit = [False] * (N+1)
group = []
for i in range(1, N+1) :
    if visit[i] : continue
    visit[i] = True
    queue = deque([i])
    sub_group = [i]
    while queue:
        t = queue.popleft()
        for j in bridge[t] :
            if not visit[j]:
                queue.append(j)
                sub_group.append(j)
                visit[j] = True
    group.append(sub_group)
print(group[0][0], group[1][0])