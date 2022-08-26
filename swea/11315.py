# 오목 판정
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    fiverock = []
    for i in range(N):
        fiverock.append(list(map(str, input())))

    res = False
    # 행 확인
    for i in range(N):
        for j in range(N - 4):
            if fiverock[i][j:j+5] == ['o'] * 5:
                res = True
                break
        if res: break

    if not res:
        # 열 확인
        for i in range(N):
            for j in range(N - 4):
                tmp = []
                for k in range(5):
                    tmp.append(fiverock[j+k][i])
                if tmp == ['o'] * 5:
                    res = True
                    break
            if res: break

    if not res:
        # 오른쪽 아래 대각선 확인
        for i in range(N - 4):
            for j in range(N - 4):
                tmp = []
                for k in range(5):
                    tmp.append(fiverock[i + k][j + k])
                if tmp == ['o'] * 5:
                    res = True
                    break
            if res: break

    if not res:
        #왼쪽 아래 대각선 확인
        for i in range(N-4):
            for j in range(N-1, 3, -1):
                tmp = []
                for k in range(5):
                    tmp.append(fiverock[i + k][j - k])
                if tmp == ['o'] * 5:
                    res = True
                    break
            if res: break

    if res:
        print(f'#{test} YES')
    else: print(f'#{test} NO')