# 신규 아이디 추천

def solution(new_id):
    answer = ''
    tmp = ''
    new_id = new_id.lower() # 1단계
    for i in new_id: # 2단계
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            tmp += i
    new_id = tmp
    tmp = ''
    i = 0
    while i < len(new_id): # 3단계
        if new_id[i] == '.':
            while i < len(new_id) and new_id[i] == '.':
                i += 1
            tmp += '.'
        else:
            tmp += new_id[i]
            i += 1

    if tmp and tmp[0] == '.': # 4단계
        tmp = tmp[1::]
    if tmp and tmp[-1] == '.':
        tmp = tmp[0:len(tmp) - 1]

    if len(tmp) == 0: # 5단계
        tmp = 'a'
    if len(tmp) >= 16: # 6단계
        tmp = tmp[0:15]
        if tmp[-1] == '.':
            tmp = tmp[0:len(tmp) - 1]
    if len(tmp) <= 2:
        s = tmp[-1]
        while len(tmp) < 3:
            tmp += s
    answer = tmp
    return answer

new_id = "=.="
print(solution(new_id))