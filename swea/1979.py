# 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    num_list = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        num_list.append(tmp)

    count = 0
    # 가로로 확인
    for i in range(N):
        for j in range(N-K+1):
            state = True
            for k in range(K): # 글자수 만큼 확인
                if num_list[i][j+k] == 0: # 중간에 0이 있다면 중단
                    state = False
                    break
            if (j <= N-K-1 and num_list[i][j+K] == 1) or(0< j and num_list[i][j-1]==1):
                state = False # 양쪽에 1이 있다면 들어갈 수 없는 곳
            if state:
                count += 1
    # 세로로 확인
    for i in range(N-K+1):
        for j in range(N):
            state = True
            for k in range(K): # 글자수 만큼 확인
                if num_list[i+k][j] == 0: # 중간에 0이 있다면 중단
                    state = False
                    break
            if (i <= N-K-1 and num_list[i+K][j] == 1) or (0< i and num_list[i-1][j]==1):
                state = False # 양쪽에 1이 있따면 들어갈 수 없는 곳
            if state:
                count += 1

    print(f'#{test} {count}')