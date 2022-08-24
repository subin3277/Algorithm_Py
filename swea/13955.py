# 너비 우선 탐색
import sys
sys.stdin = open("input.txt", "r")

def bfs(G, v):
    visited = [0] * (V + 1 )
    queue = []

    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        sol.append(t) # 정답에 추가
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[V] + 1

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    num_list = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = map(int, input().split())
        num_list[A].append(B)
        num_list[B].append(A)
    sol = []
    bfs(num_list, 1) # bfs 정점 1에서 시작
    print(f'#{test}', *sol)
