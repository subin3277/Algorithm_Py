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
    for i in range(N):
        num, *lst = map(str, input().split())
        if len(lst) == 3:
            cal[int(num)] = lst[0]
            ch1[int(num)] = int(lst[1])
            ch2[int(num)] = int(lst[2])
            par[int(lst[1])] = par[int(lst[2])] = int(num)
        else:
            cal[int(num)] = int(lst[0])

    inorder(1)
    print(stack)

    while True:
        tmp = []
        while stack:
            t = stack.pop(0)
            if type(t) == int:
                t2 = stack.pop(0)
                t3 = stack.pop(0)
                if t3 == '+':
                    tmp.append(t+t2)
                elif t3 == '-':
                    tmp.append(t-t2)
                elif t3 == '*':
                    tmp.append(t*t2)
                elif t3 == '/':
                    tmp.append(t//t2)
            else:
                tmp.append(t)
        if len(tmp) == 1:
            ans = tmp.pop()
            break
        stack = tmp.copy()

    print(f'#{test} {ans}')

    # 해결xxxxxxxxxxxxxxxxx