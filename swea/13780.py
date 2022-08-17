# 괄호 검사
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str = input()
    stack = []
    res = 1
    for i in str:
        if i == '(': # 여는 괄호면 stack에 추가
            stack.append(i)
        else: # 닫는 괄호면 그의 짝 여는 괄호 하나 삭제
            if len(stack) > 0:
                stack.pop()
            else:
                res = 0
                break

    if len(stack) != 0: # 마지막에 stack이 비어있다면 짝이 맞은 것
        res = 0
    print(f'#{test} {res}')