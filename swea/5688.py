# 세제곱근을 찾아라
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N = int(input())

    M = 0
    i = 0
    while M < N:
        i += 1
        M = i ** 3

    if M == N:
        ans = i
    else:
        ans = -1
    print(f'#{test} {ans}')