# N과 M (1)

N, M = map(int,input().split())

num = [i for i in range(1, N+1)]

def BT(result) :
    if len(result) >= M :
        print(*result)
        return
    for i in num :
        if i not in result:
            BT([*result, i])
BT([])