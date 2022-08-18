# 괄호 검사
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    stack = []
    str = input()
    res = 1
    for i in str:
        if i == '(' or i == '{': # 여는 괄호이면 stack에 추가
            stack.append(i)
        elif i == ')': # 닫는 소괄호라면
            if not stack or stack.pop() == '{': # 중괄호가 마지막에 있었다면
                res = 0 # 짝이 안맞는다
                break
        elif i == '}': # 닫는 중괄호 라면
            if not stack or stack.pop() == '(': # 소괄호가 마지막에 있었다면
                res = 0 # 짝이 안맞는다
                break
    if stack: # 모든 수행 뒤에 stack에 남아있다면
        res = 0 # 짝이 안맞는다

    print(f'#{test} {res}')