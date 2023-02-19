# 둘만의 암호

def solution(s, skip, index):
    answer = ''
    slst = list(s)
    skiplist = list(skip)

    for i in slst :
        tmp = ord(i) - 97
        j = 0
        while (j < index):
            if tmp + 1 < 123 and chr(tmp + 1) not in skiplist :
                j += 1
            elif tmp + 1 > 122:
                return
    return answer

print(solution("aukks", "wbqd", 5))