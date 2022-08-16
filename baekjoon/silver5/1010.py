# 다리 놓기
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

T = int(input())
for test in range(T):
    N, M = map(int,input().split())
    res = 1
    for i in range(M, M-N, -1):
        res *= i
    tmp = 1
    for i in range(N, 1, -1):
        tmp *= i
    res //= tmp
    print(res)