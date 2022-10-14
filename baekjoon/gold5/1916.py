# 최소비용 구하기

def dijkstra(s):
    D = adj[s][::]
    v = [0] * (N+1)
    v[s] = 1

    for _ in range(N):
        mn, i_min = 100000, 0
        for i in range(1, N+1):
            if v[i] == 0 and mn > D[i]:
                i_min, mn = i, D[i]
        v[i_min] = 1
        for i in range(1, E + 1):
            D[i] = min(D[i], D[i_min] + adj[i_min][i])

    return D[E]

N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
adj = [[100000] * (N+1) for _ in range(N + 1)]
for _ in range(M):
    A, B, k = map(int, input().split())
    adj[A][B] = k
for i in range(N + 1):
    adj[i][i] = 0
S, E = map(int, input().split())
ans = dijkstra(S)
print(ans)