# 달란트
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, P = map(int, input().split())

    res = N // P
    sol = [res] * P
    for i in range(N % P):
        sol[i] += 1
    ans = 1
    for i in range(P):
        ans *= sol[i]

    print(f'#{test} {ans}')
