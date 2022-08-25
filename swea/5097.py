# 회전
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    res = num_list[M % N]
    print(f'#{test} {res}')