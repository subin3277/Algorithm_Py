# 기능 개발
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    remain_day = [math.ceil((100-progresses[i])/speeds[i]) for i in range(N)]
    print(remain_day)
    deque_list = deque(remain_day)
    cnt = 1
    t = deque_list.popleft()
    
    while deque_list:
        if t >= deque_list[0]:
            deque_list.popleft()
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            
            if len(deque_list) == 1 :
                answer.append(cnt)
                break
            else:
                t = deque_list.popleft()
                
    if cnt > 1:
        answer.append(cnt)
    return answer