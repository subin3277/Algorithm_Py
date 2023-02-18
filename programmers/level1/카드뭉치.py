# 카드 뭉치
def solution(cards1, cards2, goal):
    answer = ''
    for i in range(len(goal)) : 
        if cards1 and cards1[0] == goal[i] :
            cards1.pop(0)
        elif cards2 and cards2[0] == goal[i] :
            cards2.pop(0)
        else :
            answer = 'No'
            break
    else :
        answer = 'Yes'
    return answer