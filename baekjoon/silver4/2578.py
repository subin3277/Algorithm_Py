# 빙고
import sys
sys.stdin = open("input.txt", "r")

def findbingo(x, y, num_list):
    state = False
    count = 0
    # 가로
    for i in range(5):
        if num_list[x][i] != 0:
            break
    else:
        count += 1
    # 세로
    for i in range(5):
        if num_list[i][y] != 0:
            break
    else:
        count += 1
    # 대각선 오른쪽 아래
    if x == y:
        for i in range(5):
            if num_list[i][i] != 0:
                break
        else:
            count += 1

    # 대각선 왼쪽 아래
    if x == 4 - y:
        for i in range(5):
            if num_list[i][4-i] != 0:
                break
        else:
            count += 1

    if count != 0:
        return True, count
    else:
        return False, count

bingo = [] # 빙고 입력 리스트
for i in range(5):
    tmp = list(map(int, input().split()))
    bingo.append(tmp)

call_num = [] # 부르는 리스트
for i in range(5):
    tmp = list(map(int, input().split()))
    call_num.append(tmp)

callcount = 0
state = False
count = 0
for i in range(5):
    for j in range(5):
        callnum = call_num[i][j]
        for k in range(5):
            if bingo[k].count(callnum) == 1: # 사회자가 부른 번호 위치 찾기
                callidx = (k, bingo[k].index(callnum))
                break
        bingo[callidx[0]][callidx[1]] = 0 # 부른 번호 0으로 바꾸기

        find = findbingo(callidx[0], callidx[1], bingo) # 빙고 됐는지 확인
        if find[0]:
            count += find[1]
        if count >= 3:
            print(i*5 + j + 1)
            state = True
            break
    if state:
        break