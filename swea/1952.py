# 수영장
import sys
sys.stdin = open("input.txt", "r")

def calu(x, k):
    global res
    if k >= res:
        return
    if x > 11:
        res = min(res, k)
        return
    if plan[x] != 0:
        if (x < 10 and plan[x+1] != 0 and plan[x+2] != 0) or (x >= 10 and not(0 in plan[x:])):
            calu(x + 3, k + price[2])
        calu(x + 1, k + price[1])
        calu(x + 1, k + price[0]*plan[x])
    else:
        calu(x + 1, k)


T = int(input())
for test in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    res = price[3]
    calu(0, 0)
    print(f'#{test} {res}')