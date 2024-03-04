# 가장 먼 노드

from collections import deque

def solution(n, edge):
    answer = 0
    
    child = [[] for _ in range(n+1)]
    for a, b in edge:
        child[a].append(b)
        child[b].append(a)

    visited = [False] * (n+1)
    visited[1] = True
    queue = deque([(1, 0)])
    cnt = 0
    res = [0] * (n+1)
    
    while queue :
        t, c = queue.popleft()
        for i in child[t]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, c+1))
                res[i] = c+1                
                
    max_res = max(res)
    answer = res.count(max_res)
            
    return answer