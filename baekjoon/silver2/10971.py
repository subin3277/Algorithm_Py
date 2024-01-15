# 외판원 순회2
N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
tmp = [i for i in range(N)]
answer = max(sum(num, [])) * N

def BT(res, sum) :
    global answer
    if len(res) == N:
        if num[res[-1]][res[0]] != 0:
            answer = min(answer, sum + num[res[-1]][res[0]])
        return
    if sum > answer:
        return
    
    for i in tmp:
        if i not in res:
            if len(res) >= 1 :
                if num[res[-1]][i] == 0:
                    return
                BT([*res, i], sum + num[res[-1]][i])
            else :
                BT([*res, i], sum)

BT([], 0)
print(answer)