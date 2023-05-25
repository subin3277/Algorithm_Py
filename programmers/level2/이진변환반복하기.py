# 이진변환 반복하기

def solution(s):
    answer = [0, 0]

    while s != "1" :
        ori_len = len(s)
        s = s.replace("0", "")
        new_len = len(s)
        answer[0] += 1
        answer[1] += ori_len-new_len
        if new_len == 1 : break
        tmp_s = new_len
        new_s = ""
        while tmp_s != 0:
            new_s = str(tmp_s%2) + new_s
            tmp_s //= 2
        s = new_s

    return answer

s = "01110"
print(solution(s))