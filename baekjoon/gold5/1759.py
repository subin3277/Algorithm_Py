# 암호 만들기

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()

def BT(idx, cnt1, cnt2, res) :
    if len(res) == L and cnt1 >= 1 and cnt2 >= 2:
        print(res)
        return
    elif len(res) == L or idx >= C :
        return
    
    nc1 = cnt1
    nc2 = cnt2
    if alpha[idx] in ['a', 'e', 'i', 'o', 'u'] :
        nc1 += 1
    else :
        nc2 += 1

    BT(idx+1, nc1, nc2, res+alpha[idx])
    BT(idx+1, cnt1, cnt2, res)
    
BT(0, 0, 0, '')