# 최소 생산 비용
import sys
sys.stdin = open("input.txt", "r")

def solution(n, k):
    global mn
    if k >= mn:
        return
    if n == N:
        mn = min(mn, k)

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            solution(n+1, k+price[n][j])
            visited[j] = False

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    price = []
    for _ in range(N):
        price.append(list(map(int, input().split())))
    mn = N * 99
    visited = [False * N for _ in range(N)]
    solution(0, 0)
    print(f'#{test} {mn}')