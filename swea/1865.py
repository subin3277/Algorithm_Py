# 동철이의 일 분배
import sys
sys.stdin = open("input.txt", "r")

def solution(n, k):
    global res
    if k == 0 or k <= res:
        return
    if n == N:
        res = max(res, k)
    for j in range(N):
        if not visited[j]:
            visited[j] = True
            solution(n+1, k*work[n][j]/100)
            visited[j] = False

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    work = []
    for _ in range(N):
        work.append(list(map(int, input().split())))
    visited = [False] * N
    res = 0
    solution(0, 1)
    print(f'#{test} {res*100:06.6f}')