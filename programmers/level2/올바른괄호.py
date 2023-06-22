#올바른 괄호

from collections import deque
def solution(s):
    answer = True
    queue = deque([])
    for i in s:
        if i == ")" and len(queue)==0:
            answer = False
            break
        elif i == ")":
            if queue.pop() == '(':
                continue
            else:
                answer = False
                break
        else:
            queue.append(i)
    if len(queue) > 0:
        answer = False
    return answer