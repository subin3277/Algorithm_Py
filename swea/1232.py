# 사칙연산
import sys
sys.stdin = open("input.txt", "r")

def inorder(n):
    global stack
    if n:
        inorder(ch1[n])
        inorder(ch2[n])
        stack.append(cal[n])
T = 10
for test in range(1, T+1):
    N = int(input())
    par = [0] * (N+1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    cal = [0] * (N + 1)
    stack = []
    # 트리 만들기
    for i in range(N):
        num, *lst = map(str, input().split())
        if len(lst) == 3:
            cal[int(num)] = lst[0]
            ch1[int(num)] = int(lst[1])
            ch2[int(num)] = int(lst[2])
            par[int(lst[1])] = par[int(lst[2])] = int(num)
        else:
            cal[int(num)] = int(lst[0])

    inorder(1) # 후위순회로 저장
    num = []
    buho = []
    while stack: # 후위표기법 연산
        t = stack.pop(0)
        if type(t) == int:
            num.append(t)
        else:
            t2 = num.pop()
            t1 = num.pop()
            if t == '+':
                num.append(t1 + t2)
            elif t == '-':
                num.append(t1 - t2)
            elif t == '*':
                num.append(t1 * t2)
            elif t == '/':
                num.append(t1 // t2)

    print(f'#{test} {num[0]}')

    # 해결xxxxxxxxxxxxxxxxx