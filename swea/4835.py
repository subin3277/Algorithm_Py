T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    minV = 1000000
    maxV = 0
    for j in range(N-M+1):
        sum = 0
        # 이웃한 숫자들 더하기
        for k in range(j, j+M):
            sum += num_list[k]
        if sum > maxV:
            maxV = sum
        if minV > sum:
            minV = sum
    # 최대 최소 차이 구하기
    res = maxV - minV
    print(f'#{i} {res}')