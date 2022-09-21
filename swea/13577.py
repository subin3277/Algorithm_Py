# 베이비진 게임
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    p = int(input())

    i = tri = runcnt = 0
    c = [0] * 12

    while i < 6:
        c[p % 10] += 1
        p = p // 10
        i += 1

    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            runcnt += 1
            continue
        i += 1
    if runcnt + tri == 2:
        print(f'#{test}', 1)
    else:
        print(f'#{test}', 0)


