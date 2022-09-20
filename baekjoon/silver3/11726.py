# 2*n 스타일링

N = int(input())
stack = [0, 1, 2]
for i in range(3, N+1):
    stack.append(stack[-2] + stack[-1])
print(stack[N] % 10007)