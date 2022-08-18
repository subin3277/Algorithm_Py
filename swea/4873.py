# 반복문자 지우기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str = input()
    stack = []
    for i in str:
        if not stack: # 빈 스택이라면
            stack.append(i) # 문자 추가
        else:
            tmp = stack.pop() # 마지막에 있는 문자 저장
            if tmp != i: # 추가할 문자와 다르다면
                stack.append(tmp) # 마지막에 꺼낸 문자 다시 추가
                stack.append(i) # 새로운 문자 추가

    print(f'#{test} {len(stack)}')