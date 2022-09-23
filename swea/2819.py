# 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open("input.txt", "r")
from itertools import product

T = int(input())
for test in range(1, T + 1):
    num = []
    for _ in range(4):
        num.append(list(map(int, input().split())))

    dire = [0, 1, 2, 3]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    res = []
    pro = []
    for p in product(dire, repeat=6):  # 이동 모든 경우의 수 구하기
        pro.append(p)

    for i in range(4):
        for j in range(4):
            for p in pro:
                x = i
                y = j
                tmp = str(num[i][j])
                for k in p:  # 경우의 수 따라 이동
                    x += dx[k]
                    y += dy[k]
                    if 0 <= x < 4 and 0 <= y < 4:  # 바깥으로 나가면 중단
                        tmp += str(num[x][y])
                    else:
                        break
                else:
                    if not (tmp in res):  # 중복 검사
                        res.append(tmp)
    print(f'#{test}', len(res))


