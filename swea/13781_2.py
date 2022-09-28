# 깊이 우선 탐색
import sys
sys.stdin = open("input.txt", "r")

def dfs(G, v):
    visited[v] = True
    res.append(v)
    for w in node[v]:
        if not visited[w]:
            dfs(G, w)

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

    visited = [False for _ in range(V + 1)]
    res = []
    dfs(node, 1)
    print(f'#{test}', *res)