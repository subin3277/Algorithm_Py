# 둘만의 암호

def solution(s, skip, index):
    answer = ''
    slst = list(s)
    skiplist = list(skip)

    for i in slst :
        tmp = ord(i)
        j = 0
        k = 1
        while (j < index):
            if tmp + 1 < 123 and chr(tmp + 1) not in skiplist :
                tmp += 1
                j += 1
            elif tmp + 1 > 122 and chr(tmp + 1 - 26) not in skiplist :
                tmp -= 25
                j += 1
            else :
                tmp += 1
        answer += chr(tmp)

    return answer

print(solution("aukks", "wbqd", 5))