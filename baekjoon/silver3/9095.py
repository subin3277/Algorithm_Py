# 1,2,3 더하기

T = int(input())
lst = []
for test in range(1, T+1):
    lst.append(int(input()))
stack = [0, 1, 2, 4]
for i in range(4, max(lst) + 1):
    stack.append(stack[-3] + stack[-2] + stack[-1])
for i in lst:
    print(stack[i])