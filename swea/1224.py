# 계산기3
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    N = int(input())
    str = input()
    num_stack = [] # 숫자, 괄호 스택
    oper_stack = [] # 부호 스택
    for i in str:
        if i == '+' or i == '*':
            oper_stack.append(i)
        elif i == '(':
            num_stack.append(i)
        elif i == ')':
            while num_stack[-2] != '(':
                sum = num_stack.pop() + num_stack.pop()
                num_stack.append(sum)
                oper_stack.pop()
            tmp = num_stack.pop() # '(' 지우기
            num_stack.pop()
            num_stack.append(tmp)
            # 괄호 앞에 곱하기가 있었다면
            if oper_stack and oper_stack[-1] == '*':
                num_stack.append(num_stack.pop() * num_stack.pop()) # 한번 더 계산
                oper_stack.pop()
        else:
            num_stack.append(int(i)) # 숫자는 추가
            # 마지막이 * 이고, 전전 값이 괄호가 아닐 때
            if oper_stack and oper_stack[-1] == '*' and len(num_stack) > 1 and num_stack[-2] != '(':
                num_stack.append(num_stack.pop()*num_stack.pop())
                oper_stack.pop()

    print(f'#{test} {num_stack[0]}')