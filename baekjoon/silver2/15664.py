# N과 M (10)
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
tmp = []

def BT(res) :
    if len(res) == M:
        if res not in tmp :
            tmp.append(res)
            print(*res)
        return

    for i in num:
        if len(res) == 0:
            BT([i])
        else :
            if res[-1] <= i and num.count(i) > res.count(i) :
                BT([*res, i])

BT([])