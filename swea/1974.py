# 스도쿠 검증
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    num_list = []
    for _ in range(9):
        tmp_list = list(map(int, input().split()))
        num_list.append(tmp_list)

    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    state = True
    for i in range(9): # 가로 한줄 확인
        for j in num_list:
            tmp_list = sorted(j) # 정렬한 리스트가
            if number != tmp_list: # 위 number 리스트와 다르면 종료
                state = False
                break
        if not state:
            break

    if state: # 세로 한줄 확인
        for i in range(9):
            tmp_list = [0]*9
            for j in range(9):
                if tmp_list[num_list[j][i]-1] != 0: # 이미 tmp_list에 값이 있다면
                    state = False # 중복된 것이니 종료
                    break
                else:
                    tmp_list[num_list[j][i]-1] = num_list[j][i] # 없으면 추가
            if not state:
                break

    # 3*3 사각형 확인
    if state:
        for i in range(3):
            tmp_list = [0]*9
            for j in range(3):
                for k in num_list[i*3+j][i*3:i*3+3]:
                    if tmp_list[k-1] != 0: # 이미 tmp_list에 값이 있다면
                        state = False # 중복된 것이니 종료
                        break
                    else :
                        tmp_list[k-1] = k # 없으면 추가
                if not state: break
            if not state: break

    if state:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')