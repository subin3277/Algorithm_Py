# 근손실
N, K = map(int, input().split())
num = list(map(int, input().split()))
tmp = [i for i in range(N)]
answer = 0

def BT(res, weight) :
    global answer
    if weight < 500 :
        return
    if len(res) == N :
        answer += 1
        return
    for i in tmp :
        if i not in res:
            BT([*res, i], weight + num[i] - K)

BT([], 500)
print(answer)