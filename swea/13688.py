# 숫자회전
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = [[] for _ in range(N)]
    for i in range(N):
        num_list[i] = list(map(str, input().split()))

    res = [[] for _ in range(3)]
    # 90도
    for i in range(N):
        res90 = ""
        for j in range(N - 1, -1, -1):
            res90 += num_list[j][i]
        res[0].append(res90)

    # 180도
    for i in range(N - 1, -1, -1):
        res180 = ""
        for j in range(N - 1, -1, -1):
            res180 += num_list[i][j]
        res[1].append(res180)

    # 270도
    for i in range(N - 1, -1, -1):
        res270 = ""
        for j in range(N):
            res270 += num_list[j][i]
        res[2].append(res270)

    print(f'#{test}') # 출력하기
    for i in range(N):
        for j in range(3):
            print(res[j][i], end=" ")
        print()