# 체육복

def solution(n, lost, reserve):
    answer = 0
    can = [False] * n
    lost.sort()
    reserve.sort()
    
    for i in range(1, n+1):
        if i not in lost:
            can[i-1] = True
        elif i in lost and i in reserve:
            can[i-1] = True
            reserve.remove(i)
    reserve_copy= reserve.copy()
    for i in reserve:            
        if i in lost:
            lost.remove(i)
        elif i>1 and i-1 in lost:
            can[i-2] = True
            lost.remove(i-1)
        elif i < n and i+1 in lost:
            can[i] = True
            lost.remove(i+1)
    answer = can.count(True)
    return answer