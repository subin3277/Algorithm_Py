# N과 M (3)

N, M = map(int,input().split())

num = [i for i in range(1, N+1)]

def BT(result) :
    if len(result) >= M :
        print(*result)
        return
    for i in num :
        BT([*result, i])
BT([])