# 숫자 만들기
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def dfs(v):
    if v == N - 1:
        tmp = num[0]
        for i in range(N - 1):
            if stack[i] == 0:
                tmp += num[i + 1]
            elif stack[i] == 1:
                tmp -= num[i + 1]
            elif stack[i] == 2:
                tmp *= num[i + 1]
            elif stack[i] == 3:
                if tmp >= 0:
                    tmp //= num[i + 1]
                else:
                    tmp = -tmp
                    tmp //= num[i + 1]
                    tmp = -tmp
        res.append(tmp)
        return

    for i in range(4):
        if operation[i] > 0:
            stack.append(i)
            operation[i] -= 1
            dfs(v + 1)
            operation[i] += 1
            stack.pop()



T = int(input())
for test in range(1, T + 1):
    N = int(input())
    operation = list(map(int, input().split()))
    num = list(map(int, input().split()))
    stack = deque()
    res = []
    dfs(0)
    print(f'#{test} {max(res) - min(res)}')