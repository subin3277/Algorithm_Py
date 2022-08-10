import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    # 빈 이차원 리스트 생성
    num_list = []
    for _ in range(N):
        num_list.append([0]*N)

    # 우하좌상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    res = 1 # 리스트에 담을 값
    k = 0 # di, dj의 index
    ni = nj = 0
    for i in range(N*N):
        num_list[ni][nj] = res
        res += 1
        ni += di[k] # 우하좌상 이동
        nj += dj[k] # 우하좌상 이동
        # 이동한 곳이 N의 범위를 넘거나 이미 값이 있는 곳이라면
        if not(0 <= ni < N) or not(0 <= nj < N) or num_list[ni][nj] != 0:
            # 다시 돌아간다
            ni -= di[k]
            nj -= dj[k]
            # k의 값을 1더해 방향을 바꾼다(3일때는 0으로 이동)
            if k == 3:
                k = 0
            else:
                k += 1
            # 다시 이동한다
            ni += di[k]
            nj += dj[k]

    print(f'#{test}')
    for i in num_list:
        print(*i)