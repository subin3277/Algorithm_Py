# 암호문3
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T + 1):
    N = int(input())
    secret = list(map(str, input().split()))
    M = int(input())
    todo = list(map(str, input().split()))
    i = 0
    count = 0
    while count < M:
        if todo[i] == 'I': # I이면
            x = int(todo[i + 1]) # x, y값 꺼내고
            y = int(todo[i + 2])
            k = 3
            for j in range(x, x+y):
                secret.insert(j, todo[i+k]) # j의 위치에 하나씩 삽입
                k += 1
            i += 3 + y # 명령어 인덱스 옮기기
        elif todo[i] == 'D': # D이면
            x = int(todo[i+1])
            y = int(todo[i+2])
            for j in range(x, x+y):
                secret.pop(x) # x위치에 있는 값 삭제
            i += 3
        elif todo[i] == 'A': # A이면
            y = int(todo[i + 1])
            for j in range(y):
                secret.append(todo[i + 2 + j]) # 맨뒤에 값 추가
            i += 2 + y
        count += 1

    sol = secret[0:10] # 10개만 출력
    print(f'#{test}', *sol)