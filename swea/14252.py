# 최단경로
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N ,E = map(int, input().split())
    node = [[] for _ in range(N)]
    for _ in range(E):
        A, B, V = map(int, input().split())
        node[A].append((B, V))
    # N -1번 노드까지 가야함
    queue = [(0, 0)]
    visited = [False for _ in range(N)]
    res = []
    while queue:
        t = queue.pop(0)
        for i in node[t[0]]:
            if not visited[i[0]]:
                if i[0] == N-1:
                    res.append(t[1] + i[1])
                else:
                    visited[i[0]] = True
                    queue.append([i[0], i[1]+t[1]])
    print(f'#{test}', min(res))