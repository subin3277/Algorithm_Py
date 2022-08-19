# Magnetic
import sys
sys.stdin = open("input.txt", "r")

# 1은 N극 2는 S극 위 N 아래 S
T = 10
for test in range(1, T+1):
    N = int(input())
    mag_list = []
    for i in range(100):
        tmp = list(map(int, input().split()))
        mag_list.append(tmp)

    count = 0
    for i in range(100):
        stack = []
        for j in range(100):
            tmp = mag_list[j][i] # 넣을 값
            if not stack and tmp == 2: # 스택이 비어있고, S극을 넣는다면
                pass # 아무일 일어나지 않음
            elif stack and tmp == 2 and stack[-1] == 1: # 스택에 2를 넣고, 마지막 값이 1이라면
                stack.append(tmp)
                count += 1 # 교착상태 1 추가
            elif tmp != 0:
                stack.append(tmp)

    print(f'#{test} {count}')