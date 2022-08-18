# 그래프 경로
import sys
sys.stdin = open("input.txt", "r")

def dfs(v, G):
    while True:
        for w in num_list[v]:
            if w == G:  # 방문한곳이 목표지점과 같다면
                return 1  # 1 반환하며 종료

            if not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    N = V+1
    num_list = [[] for _ in range(N)]
    for i in range(E):
        A, B = map(int, input().split())
        num_list[A].append(B)
    S, G = map(int, input().split())
    visited = [False] * N
    stack = []

    res = dfs(S, G)
    print(f'#{test} {res}')