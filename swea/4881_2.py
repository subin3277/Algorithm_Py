# 배열 최소 합
import sys
sys.stdin = open("input.txt", "r")

def perm(n, k):
    global mn
    if k >= mn:
        return
    if n == N:
        mn = min(mn, k)

    for j in range(N):
        if not used[j]:
            used[j] = True
            perm(n+1, k+lst[n][j])
            used[j] = False

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    mn = 10*N

    a = [i for i in range(N)]
    used = [False for _ in range(N)]
    p = [0] * N
    perm(0, 0)
    print(f'#{test} {mn}')