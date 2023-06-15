# 모의고사

def solution(answers):
    answer = []
    sol1 = [1, 2, 3, 4, 5]
    sol2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = cnt2 = cnt3 = 0
    
    for i in range(len(answers)):
        ans = answers[i]
        if ans == sol1[i%5] :
            cnt1 += 1
        if ans == sol2[i%8]:
            cnt2 += 1
        if ans == sol3[i%10]:
            cnt3 += 1
    if max(cnt1, cnt2, cnt3) == cnt3:
        if cnt1 == cnt3:
            answer.append(1)
        if cnt2 == cnt3:
            answer.append(2)
        answer.append(3)
    elif max(cnt1, cnt2, cnt3) == cnt2:
        if cnt1 == cnt2:
            answer.append(1)
        answer.append(2)
        if cnt2 == cnt3:
            answer.append(3)
    elif max(cnt1, cnt2, cnt3) == cnt1:
        answer.append(1)
        if cnt1 == cnt2:
            answer.append(2)
        if cnt1 == cnt3:
            answer.append(3)
            
    return answer