# 문자열 폭발
from collections import deque

str = input()
t = input()

stack = deque()
idx = 0
for i in str :
    stack.append(i)
    for j in range(len(t)) :
        if stack[len(stack) - j - 1] == t[len(t) - j - 1] :
            continue
        else :
            break
    else :
        for j in range(len(t)) :
            stack.pop()

result = ''.join(stack)
if result == '' :
    print('FRULA')
else :
    print(result)