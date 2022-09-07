# 숫자 문자열과 영단어

def solution(s):
    answer = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
        else:
            if s[i] == 'z':
                answer += '0'
                i += 3
            elif s[i] == 'o':
                answer += '1'
                i += 2
            elif s[i] == 't':
                if s[i+1] == 'h':
                    answer += '3'
                    i += 4
                else:
                    answer += '2'
                    i += 2
            elif s[i] == 'f':
                if s[i+1] == 'i':
                    answer += '5'
                else:
                    answer += '4'
                i += 3
            elif s[i] == 's':
                if s[i + 1] == 'i':
                    answer += '6'
                    i += 2
                else:
                    answer += '7'
                    i += 4
            elif s[i] == 'e':
                answer += '8'
                i += 4
            elif s[i] == 'n':
                answer += '9'
                i += 3
        i += 1
    answer = int(answer)
    return answer

s="one4seveneight"
print(solution(s))