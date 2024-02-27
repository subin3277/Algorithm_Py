# 1 빼기

N = int(input())
answer = N + 1

def BT(res, cnt, log) :
    global answer
    if res == 0 :
        answer = min(answer, cnt)
        return

    if cnt > answer :
        return

    str_res = str(res)
    if '1' in str_res:
        str_res = str_res.replace('1', '', 1)
        if str_res == '' :
            new_res = 0
        else :
            new_res = int(str_res)
        BT(new_res, cnt + 1, [*log, new_res])

    BT(res - 1, cnt + 1, [*log, res - 1])

BT(N, 0, [N])
print(answer)