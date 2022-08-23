# Forth
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str_list = list(map(str, input().split()))
    stack = []
    for i in str_list:
        if i == '.': # .이 나오면 출력
            if len(stack) == 1:
                res = stack[-1]
            else:
                res = 'error'
            break
        elif len(stack) > 1 and i == '+': # stack에 2개 이상이 있고, +를 만나면
            stack.append(stack.pop() + stack.pop())
        elif len(stack) > 1 and i == '*': # stack에 2개 이상 있고, *를 만나면
            stack.append(stack.pop() * stack.pop())
        elif len(stack) > 1 and i == '-': # stack에 2개 이상 있고, -를 만나면
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif len(stack) > 1 and i == '/': # stack에 2개 이상 있고,/를 만나면
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        else:
            if i == '+' or i == '*' or i == '-' or i == '/': # + or * or - or /를 만났는데 stack에 원소가 2개 미만이면
                res = 'error' # 에러 출력
                break
            stack.append(int(i))

    print(f'#{test} {res}')
