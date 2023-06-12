# 완주하지 못한 선수

def solution(participant, completion):
    d = {}
    for i in participant:
        d[i] = d.get(i, 0) + 1
    
    for i in completion:
        d[i] -= 1
        
    ans = [k for k, v in d.items() if v > 0]
    answer = ans[0]
    return answer