# 농작물 수확하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = []
    for i in range(N):
        tmp = input()
        tmp_list = []
        for j in tmp:
            tmp_list.append(int(j))
        num_list.append(tmp_list)

    count = 0
    for i in range(N//2):
        for j in range(N//2 - i, N//2 + i + 1): # 가운데부터 양쪽으로
            count += num_list[i][j]
            count += num_list[N - i - 1][j]
    for i in range(N):
        count += num_list[N//2][i] # 가운데 값 더해주기
    print(f'#{test} {count}')