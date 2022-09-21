# 부분집합의 합
import sys
sys.stdin = open("input.txt", "r")

def com(n, r, s):
    global cnt
    if r == 0:
        if sum(comb) == K:
            cnt += 1
    else:
        for i in range(s, n - r + 1):
            comb[r-1] = A[i]
            com(n, r-1, i+1)
T = int(input())
for test in range(1, T+1):
    N , K = map(int, input().split())
    A = [i for i in range(1, 13)]

    comb = [0] * 13
    cnt = 0
    com(12, N, 0)
    print(f'#{test}', cnt )

