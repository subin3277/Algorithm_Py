# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    prev=" "
    for i in s:
        if prev == ' ' and i.isascii():
            answer += i.upper()
        else:
            answer += i.lower()
        prev = i
    return answer

s = "3people unFollowed me"
print(solution(s))