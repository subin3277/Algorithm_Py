# N과 M(7)
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

def BT(index, result) :
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        BT(i, [*result, num[i]])

BT(0, [])