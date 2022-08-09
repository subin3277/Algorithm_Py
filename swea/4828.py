T = int(input())

for i in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    # 버블 정렬 이용하여 정렬
    for j in range(N-1, 0, -1):
        for k in range(0, j):
            if num_list[k] > num_list[k+1]:
                num_list[k], num_list[k+1] = num_list[k+1], num_list[k]
    # 두 값의 차이 구하기
    res = num_list[N-1] - num_list[0]
    print(f'#{i} {res}')