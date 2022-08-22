# 계산기2
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    strlen = int(input())
    str = input()
    res = 0
    stack = [] # 숫자 저장할 스택
    stack2 = [] # 부호 저장할 스택
    for i in str:
        if i == '+' or i == '*':
            stack2.append(i)
        else:
            stack.append(int(i))
            if stack2 and stack2[-1] == '*': # 전의 부호가 *이면
                stack.append(stack.pop() * stack.pop()) # 두 수 곱하기
    for i in stack:
        res += i # stack에 있는 모든값 더하기
    print(f'#{test}', res)