# 종이 붙이기
import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for test in range(1, T+1):
    N = int(input())
    stack = [0, 1, 3]
    for i in range(3, N//10 + 1):
        stack.append(stack[-2] * 2 + stack[-1])

    print(f'#{test} {stack[N//10]}')