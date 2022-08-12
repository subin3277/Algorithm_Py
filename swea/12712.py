# 파리퇴치3
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    num_list = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        num_list.append(tmp)

    res = 0

    # + 모양 분사
    for i in range(N):
        for j in range(N):
            k = 1
            sum = num_list[i][j]
            # 위로
            while 0 <= i-k and k < M:
                sum += num_list[i-k][j]
                k += 1
            k = 1
            # 아래로
            while i+k < N and k < M:
                sum += num_list[i+k][j]
                k += 1
            k = 1
            # 왼쪽으로
            while 0 <= j-k and k < M:
                sum += num_list[i][j-k]
                k += 1
            k = 1
            # 오른쪽으로
            while j+k < N and k < M:
                sum += num_list[i][j+k]
                k += 1

            if res < sum:
                res = sum

    # x 모양 분사
    for i in range(N):
        for j in range(N):
            k = 1
            sum = num_list[i][j]
            # 왼쪽 위로
            while 0 <= i-k and 0 <= j-k and k < M:
                sum += num_list[i-k][j-k]
                k += 1
            k = 1
            # 오른쪽 위로
            while 0 <= i - k and N > j + k and k < M:
                sum += num_list[i - k][j + k]
                k += 1
            k = 1
            # 왼쪽 아래로
            while N > i + k and 0 <= j - k and k < M:
                sum += num_list[i + k][j - k]
                k += 1
            k = 1
            # 오른쪽 아래로
            while N > i + k and N > j + k and k < M:
                sum += num_list[i + k][j + k]
                k += 1

            if res < sum:
                res = sum
    print(f'#{test} {res}')