# Ladder2
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T + 1):
    N = int(input())
    ladder = []
    # 이차원 배열 생성
    for j in range(100):
        tmp = list(map(int, input().split()))
        # 범위 벗어나는 것을 방지하기 위해 양끝에 0 추가
        tmp.append(0)
        tmp.insert(0, 0)
        ladder.append(tmp)

    min_count = [-1, 10000]
    for j in range(1, 101):
        count = 2
        # 출발점이 0이라면 다음 줄로
        if ladder[0][j] == 0:
            continue
        y = j
        x = 1

        # 사다리 맨 밑에 내려갈때까지
        while x < 100:
            # 오른쪽에 길이 있다면
            if ladder[x][y + 1] == 1:
                # 1이 끝나는 길까지
                while ladder[x][y + 1] == 1:
                    # 오른쪽으로 이동
                    y += 1
                    count += 1
            # 왼쪽에 길이 있다면
            elif ladder[x][y - 1] == 1:
                # 1이 끝나는 길까지
                while ladder[x][y - 1] == 1:
                    # 왼쪽으로 이동
                    y -= 1
                    count += 1
            # 한줄 밑으로 이동
            x += 1
            count += 1

        if min_count[1] > count:
            min_count[0] = j - 1
            min_count[1] = count

    print(f'#{test} {min_count[0]}')