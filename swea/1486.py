# 장훈이의 높은 선반
import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations

T = int(input())
for test in range(1, T + 1):
    N, B = map(int, input().split())
    tall = list(map(int, input().split()))

    tall.sort()
    tmp = 0
    x = -1
    while True:
        if tmp >= B:
            break
        tmp += tall[x]
        x -= 1
    x = -x - 1
    res = []
    ans = 0
    state = True
    for i in range(x, N + 1):
        for c in combinations(tall, i):
            if sum(c) > B:
                res.append(sum(c) - B)
            elif sum(c) == B:
                ans = 0
                state = False
                break
        if not state:
            break
    if state:
        ans = min(res)
    print(f'#{test} {ans}')