# 후위표기법 변환
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str = input()
    stack = [] # 답 저장할 stack
    stack2 = [] # 부호 저장할 stack

    for i in str:
        if i == '*': # 곱하기이면
            stack2.append(i) # 부호 stack에 저장
            continue
        elif i == '+': # 더하기이면
            stack2.append(i)

        else: # 숫자라면
            stack.append(i)

        # 이전의 부호가 * 였다면 or 이전의 부호가 +이고 stack2길이는 1보다 클때
        if (stack2 and stack2[-1] == '*') or (len(stack2) > 1 and stack2[-1] == '+'):
            a = stack[-2]
            b = stack[-1]
            stack.pop()
            stack.pop()
            stack.append(a + b + stack2.pop()) # 부호와 함께 다시 저장

    print(f'#{test}', stack[-2]+stack[-1]+stack2.pop())

