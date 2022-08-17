# 파스칼 삼각형
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    stack = []
    print(f'#{test}')
    for i in range(N):
        tmp = stack.copy()
        stack = []
        num2 = 0
        while True:
            num1 = num2
            if tmp:
                num2 = tmp.pop() # 새로운 값 꺼내서
                stack.append(num1+num2) # 더하기
            else:
                stack.append(1) # 더이상 없으면 1 삽입
                break
        print(*stack)