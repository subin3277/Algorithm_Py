# 전자카트
import sys
sys.stdin = open("input.txt", "r")

from itertools import permutations

T = int(input())
for test in range(1, T+1):
    N = int(input())
    battery = []
    for _ in range(N):
        battery.append(list(map(int, input().split())))
    lst = [i for i in range(1, N)]
    res = 100 * N
    for p in permutations(lst): # 모든 순열 구하기
        tmp = battery[0][p[0]]
        for i in range(N - 2):
            tmp += battery[p[i]][p[i+1]]
            if tmp > res:
                break
        else:
            tmp += battery[p[-1]][0]
            res = min(res, tmp)
    print(f'#{test} {res}')