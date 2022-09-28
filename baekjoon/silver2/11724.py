# 연결요소의 개수
from collections import deque
def search(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        t = queue.popleft()
        for i in node[t]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    node[A].append(B)
    node[B].append(A)

visited = [False] * (N + 1)
res = 0

for i in range(1, N + 1):
    if not visited[i]:
        if not node[i]:
            res += 1
            visited[i] = True
        else:
            search(i)
            res += 1
print(res)

