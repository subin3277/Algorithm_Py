# 최대 상금
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    num, N = map(str, input().split())
    lst = list(map(int, num))
    ori = list(map(int, num))
    N = int(N)
    ori.sort()
    ori.reverse()

    rep = [i for i in range(len(num)) if lst.count(lst[i]) > 1]
    fix = exchange = 0
    while exchange < N and ori != lst:
        max_res = max(lst[fix::])
        max_idx = lst.index(max_res,fix,len(lst))
        if max_idx == fix:
            fix += 1
            continue
        # if lst[fix::].count(lst[max_idx]) != 1:
        #     tmp = lst[fix::]
        #     tmp.reverse()
        #     tmp_idx = tmp.index(max_res)
        #     max_idx = -tmp_idx -1
        lst[max_idx], lst[fix] = lst[fix], lst[max_idx]
        exchange += 1
        fix += 1

    if exchange == N:
        lst2 = sorted([lst[i] for i in rep], reverse=True)
        for i in rep:
            lst[i] = lst2.pop(0)
    elif (N - exchange)%2 == 1 and not rep:
            for i in lst:
                if lst.count(i) >= 2:
                    break
            else:
                lst[-1], lst[-2] = lst[-2], lst[-1]

    print(f'#{test}', end=" ")
    print(*lst, sep="")

