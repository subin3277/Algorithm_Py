# 2*n 타일링 2

N = int(input())
stack = [0, 1, 3, 5]
i = 3
while i < N:
    stack.append(stack[-1] + stack[-2]*2)
    i += 1
print(stack[N]%10007)