# 비밀번호
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    N, num = map(str, input().split())
    stack = []
    for i in num:
        if not stack:  # 빈 스택이라면
            stack.append(i)  # 문자 추가
        else:
            tmp = stack.pop()  # 마지막에 있는 문자 저장
            if tmp != i:  # 추가할 문자와 다르다면
                stack.append(tmp)  # 마지막에 꺼낸 문자 다시 추가
                stack.append(i)  # 새로운 문자 추가
    res = ""
    for i in stack:
        res += i
    print(f'#{test} {res}')