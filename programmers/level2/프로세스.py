# 프로세스

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        if location == 0 and max(queue) == queue[0]:
            answer += 1
            break
        elif max(queue) == queue[0]:
            queue.popleft()
            location -= 1
            answer += 1
        else:
            t = queue.popleft()
            queue.append(t)
            if location == 0 :
                location = len(queue)
            location -= 1
    return answer