# 회문
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    str_list = []

    for i in range(N):
        str = input()
        str_list.append(str)
    # 가로 확인
    for i in range(N):
        for j in range(N-M+1):
            x = j
            y = j + M - 1
            state = True
            while x != y and x-1 != y: # 양쪽에서 가운데로 확인
                if str_list[i][x] != str_list[i][y]: # 하나라도 다르면 회문 x
                    state = False
                    break
                else: # x는 다음값, y는 앞으로
                    x += 1
                    y -= 1
            if state:
                print(f'#{test} {str_list[i][j:j+M]}')
                break
        if state:
            break

    # 세로 확인
    if not state:
        for i in range(N):
            for j in range(N-M+1):
                x = j
                y = j+M-1
                state = True
                while x != y and x - 1 != y:
                    if str_list[x][i] != str_list[y][i]:
                        state = False
                        break
                    else:
                        x += 1
                        y -= 1
                if state:
                    res = ""
                    for k in range(j,j+M):
                        res += str_list[k][i]
                    print(f'#{test} {res}')
                    break
            if state:
                break