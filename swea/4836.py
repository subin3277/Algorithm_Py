# 색칠하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    #  10*10 이차원 리스트 생성
    color_list = [[0]*10 for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 입력받은 범위에 color 수
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # 이미 색칠된 곳이고 앞으로 칠할 색깔과 다르다면
                if color_list[r][c] != 0 and color_list[r][c] != color:
                    # 보라색 3으로
                    color_list[r][c] = 3
                else :
                    # 아니면 입력 색깔
                    color_list[r][c] = color
    for i in range(10) :
        for j in range(10):
            if color_list[i][j] == 3:
                count += 1
    print(f'#{test} {count}')