#델타검색
import sys
sys.stdin = open("input.txt", "r")

# 절댓값 구하는 함수
def sumnum(N, a):
    # a가 빈곳이라면 0을 리턴
    if a==0:
        return 0
    else:
        res = N-a
        # 뺀 값이 음수라면
        if res < 0:
            # 양수로 바꾸기
            res = -res
        return res

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        num_list.append(tmp)

    res = 0
    # 가로로 이웃한 차의 절댓값
    for i in range(N):
        for j in range(N-1):
            res += sumnum(num_list[i][j], num_list[i][j+1])

    # 세로로 이웃한 차의 절댓값
    for i in range(N):
        for j in range(N-1):
            res += sumnum(num_list[j][i], num_list[j+1][i])
    # 상하좌우 계산하면 모든 절댓값에 *2 해주면 된다.
    print(f'#{test} {res*2}')