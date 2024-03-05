from collections import deque

def solution(cards):
    answer = 0
    visit = [False] * (len(cards) + 1)
    queue = deque()
    group = []
    for i in cards :
        if visit[i] :
            continue
        queue.append(i)
        visit[i] = True
        sub_group = [i]
        while queue :
            t = queue.popleft()
            if not visit[cards[t-1]] :
                visit[cards[t-1]] = True
                queue.append(cards[t-1])
                sub_group.append(cards[t-1])
            else :
                group.append(sub_group)
                break
    group.sort(key=len, reverse = True)
    if len(group) < 2:
        answer = 0
    else:
        answer = len(group[0]) * len(group[1])
    return answer