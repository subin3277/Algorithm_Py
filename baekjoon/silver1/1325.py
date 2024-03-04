# 효율적인 해킹

from collections import deque

N, M = map(int, input().split())
child = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    child[b].append(a)

ans = []
max_res = 0

for i in range(1, N + 1):
    visit = [False] * (N + 1)
    visit[i] = True
    queue = deque([i])
    cnt = 1
    while queue :
        t = queue.popleft()
        for j in child[t] :
            if not visit[j] :
                cnt+=1
                visit[j] = True
                queue.append(j)

    if cnt > max_res :
        max_res = cnt
        ans = [i]
    elif cnt == max_res:
        ans.append(i)

print(*ans)