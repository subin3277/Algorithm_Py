# N과 M(6)
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

def BT(index, result) :
    if len(result) == M:
        print(*result)
        return
    for i in range(index, N):
        if num[i] not in result:
            BT(i+1, [*result, num[i]])

BT(0, [])