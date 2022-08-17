# 깊이 우선 탐색
import sys
sys.stdin = open("input.txt", "r")

def DFS(v):
    stack = []
    visited = [False]*(V+1)

    visited[v] = True
    sol.append(v)
    while True:
        for w in adjList[v]: # w와 연결된 곳
            if not visited[w]: # 방문하지않은 곳이면
                stack.append(v) # 돌아올 곳을 push
                v = w # 기준점 바꾸기
                visited[w] = True # 방문 체크
                sol.append(w)
                break
        else: # 방문가능한 곳이 없다면
            if stack: # 비어 있지 않다면
                v = stack.pop()
            else: # 비어 있다면
                break

T = int(input())
for test in range(1, T+1):
    V , E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = list(map(int,input().split()))
        adjList[A].append(B)
        adjList[B].append(A)

    sol = []
    DFS(1)
    print(f'#{test}', *sol)
