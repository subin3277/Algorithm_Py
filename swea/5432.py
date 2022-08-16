# 쇠막대기 자르기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str = input()
    stack = []
    count = res = 0
    prev = '' # 이전에 있던 항목
    for i in str:
        if i == '(': # '('라면 stack에 추가후 count 1 추가
            stack.append(i)
            count += 1
        else: # ')'라면
            count -= 1 # count 1 감소
            stack.pop() # '('하나 삭제
            if prev == '(': # ')'를 연속으로 입력 받은게 아니라면
                res += count # 레이저로 자른 부분
            else:
                res += 1 # 막대기가 끝나는 부분
        prev = i
    print(f'#{test} {res}')