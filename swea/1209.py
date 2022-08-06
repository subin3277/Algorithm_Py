T = 1

for i in range(T) :
    N = int(input())
    num_list = []
    for j in range(100) :
        tmp = list(map(int,input().split()))
        num_list.append(tmp)

    maxres = 0
    # 가로 덧셈
    for j in num_list :
        maxres = max(maxres,sum(j))

    # 세로 덧셈
    for j in range(100) :
        sumres = 0
        for k in range(100):
            sumres += num_list[k][j]
        maxres = max(maxres,sumres)

    # 대각선
    sumres1 = 0
    sumres2 = 0
    for j in range(100) :
        # 오른쪽 아래
        sumres1 += num_list[j][j]
        # 왼쪽 아래
        sumres2 += num_list[j][99-j]
    maxres = max(maxres,sumres1,sumres2)

    print(f'#{N} {maxres}')