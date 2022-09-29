# 최소 이동 거리
import sys
sys.stdin = open("input.txt", "r")

def dijkstra(s):
    D = adj[s][::]
    v = [0] * (N+1)
    v[s] = 1

    for _ in range(N):
        mn, i_min = 500, 0
        for i in range(N+1):
            if v[i] == 0 and mn > D[i]:
                i_min, mn = i, D[i]
        v[i_min] = 1
        for i in range(N+1):
            D[i] = min(D[i], D[i_min] + adj[i_min][i])

    return D[N]

T = int(input())
for test in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[500]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    for i in range(N+1):
        adj[i][i] = 0
    ans = dijkstra(0)
    print(f'#{test} {ans}')

    # node = [[] for _ in range(N + 1)]
    # for _ in range(E):
    #     A, B, V = map(int, input().split())
    #     node[A].append((B, V))
    # print(node)
    # # N번 노드까지 가야함
    # queue = [(0, 0)]
    # visited = [False for _ in range(N+1)]
    # res = []
    # while queue:
    #     t = queue.pop(0)
    #     for i in node[t[0]]:
    #         if not visited[i[0]]:
    #             if i[0] == N:
    #                 res.append(t[1] + i[1])
    #             else:
    #                 queue.append([i[0], i[1] + t[1]])
    # print(res)
    # print(f'#{test}', min(res))