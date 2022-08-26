# 괄호 짝짓기
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    N = int(input())
    strlist = input()
    stack = []
    res = 1
    for i in strlist:
        if i == ')':
            if not stack or stack.pop() != '(':
                res = 0
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                res = 0
                break
        elif i == '}':
            if not stack or stack.pop() != '{':
                res = 0
                break
        elif i == '>':
            if not stack or stack.pop() != '<':
                res = 0
                break
        else:
            stack.append(i)
    if len(stack) != 0:
        res = 0
    print(f'#{test} {res}')