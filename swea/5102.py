# 노드의 거리
import sys
sys.stdin = open("input.txt", "r")

def bfs(S, G, n):
    visitied = [False] * n
    queue = []
    queue.append((S, 0)) # (노드 값, 방문 몇번째)
    visitied[S] = True
    count = 0
    while queue:
        t = queue.pop(0) # 맨 앞값 꺼내기
        if t[0] == G: # 도착점과 같으면
            count = t[1] # 그동안 지난 간선 개수
            return count

        tmpcount = 0
        for w in node[t[0]]:
            if not visitied[w]:
                queue.append((w, t[1] + 1)) # 지난 간선 개수 하나 증가 후 추가
                visitied[w] = True

    return 0


T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    for i in range(E):
        A, B = map(int, input().split())
        node[A].append(B)
        node[B].append(A)
    S, G = map(int, input().split())
    res = bfs(S, G, V + 1)

    print(f'#{test} {res}')