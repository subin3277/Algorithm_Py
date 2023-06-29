# 카펫

def solution(brown, yellow):
    answer = []
    xplusy = brown//2 + 2
    xmultiy = brown+yellow
    
    for i in range(xplusy//2, 1, -1):
        x = i
        y = xplusy - x
        if x*y == xmultiy:
            answer = [y, x]
            break
    return answer