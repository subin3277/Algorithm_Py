# 부분집합
import sys
sys.stdin = open("input.txt", "r")

def backtrack(i, N, K):
    global count

    if i == N:
        res = 0
        for i in range(N):
            if bit[i]:
                res += A[i] # 더한값이 K와 같다면
        if res == K:
            count += 1 # count 1 증가
    else:
        bit[i] = 1
        backtrack(i+1, N, K)
        bit[i] = 0
        backtrack(i+1, N, K)

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    bit = [0] * N
    count = 0
    backtrack(0, N, K)
    print(f'#{test} {count}')