# 부등호

K = int(input())
sign = list(map(str, input().split()))
num = [i for i in range(10)]
max_answer = '0'
min_answer = '9987654321'

def BT(res) :
    global max_answer, min_answer
    if len(res) > K :
        max_answer = max(max_answer, ''.join(str(s) for s in res))
        min_answer = min(min_answer, ''.join(str(s) for s in res))
        return

    idx = len(res)
    if idx == 0:
        for i in num :
            BT([i])
    elif sign[idx - 1] == '<':
        for i in range(res[-1] + 1, 10):
            if i not in res:
                BT([*res, i])
    elif sign[idx - 1] == '>':
        for i in range(res[-1]):
            if i not in res:
                BT([*res, i])

BT([])
print(max_answer)
print(min_answer)