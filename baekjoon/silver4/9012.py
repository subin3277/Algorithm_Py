# 괄호

N = int(input())
for _ in range(N):
    str = input()
    stack = []
    state = True
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                t = stack.pop()
            else:
                state = False
                break
    if stack:
        state = False
    
    if state:
        print("YES")
    else:
        print("NO")