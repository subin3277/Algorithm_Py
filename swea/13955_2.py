# 너비우선 탐색
import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test in range(1, T + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    for _ in range(E):
        A, B = map(int, input().split())
        node[A].append(B)
        node[B].append(A)
    for i in node:
        i.sort()

    queue = [1]
    visited = [False for _ in range(V + 1)]
    visited[1] = True
    res = []
    while queue:
        t = queue.pop(0)
        for i in node[t]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        res.append(t)
    print(f'#{test}', *res)