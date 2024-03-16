# 영재의 시험
ans = list(map(int, input().split()))
cnt = 0

def BT(idx, pre, score, same) :
    global cnt
    if idx == 10 and score >= 5 :
        cnt += 1
        return
    if idx == 10 or score + (10 - idx) < 5 :
        return
    
    for i in range(1, 6):
        if pre == i:
            ns = same + 1
        else :
            ns = 1

        if ns >= 3:
            continue

        if i == ans[idx]:
            BT(idx+1, i, score+1, ns)
        else :
            BT(idx+1, i, score, ns)

BT(0, -1, 0, 0)
print(cnt)