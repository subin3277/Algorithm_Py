# 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    type = [0, 0, 0, 0]
    ori_type = ['RT', 'CF', 'JM', 'AN']
    for i in range(len(survey)):
        if 'R' in survey[i]:
            idx = 0
        elif 'C' in survey[i]:
            idx = 1
        elif 'J' in survey[i]:
            idx = 2
        elif 'A' in survey[i]:
            idx = 3

        if survey[i][0] < survey[i][1]:
            type[idx] += choices[i] - 4
        else:
            type[idx] -= choices[i] - 4
    for i in range(4):
        if type[i] > 0:
            answer += ori_type[i][1]
        else:
            answer += ori_type[i][0]
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"] # RT, CF, JM, AN
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))