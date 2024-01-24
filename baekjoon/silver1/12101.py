# 1,2,3 더하기 2
N, K = map(int, input().split())

cnt = 0

def BT(num, res) :
    global cnt
    if num == 0 :
        cnt += 1
        if cnt == K :
            print('+'.join(map(str, res)))
        return 
    
    if cnt == K :
        return 
    
    BT(num - 1, [*res, 1])

    if num >= 2 :
        BT(num -2, [*res, 2])
    
    if num >= 3 :
        BT(num-3, [*res, 3])

BT(N, [])
if cnt < K :
    print(-1)
