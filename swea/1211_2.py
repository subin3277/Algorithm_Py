# Ladder2
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    testnum = int(input())
    ladder_list = []
    for i in range(100):
        tmp = [0] + list(map(int, input().split())) + [0]
        ladder_list.append(tmp)

    min_count = [-1, 10000] # 최소의 [위치, 최소값]

    for i in range(1, 101):
        count = 0
        if ladder_list[0][i] == 0: # 시작점이 0이라면 다음으로
            continue

        x = 1
        y = i
        while x < 100: # 맨 밑에 내려갈 동안
            if ladder_list[x][y+1] == 1: # 오른쪽에 1이 있다면
                while ladder_list[x][y+1] != 0: # 안나올 때 까지
                    y += 1
                    count += 1

            elif ladder_list[x][y-1] == 1: # 왼쪽에 1이 있다면
                while ladder_list[x][y-1] != 0: # 안나올 때 까지
                    y -= 1
                    count += 1

            x += 1
            count += 1

        if min_count[1] > count:
            min_count[0] = i - 1
            min_count[1] = count


    print(f'#{test} {min_count[0]}')