T = int(input())

for i in range(1, T+1):
    N = int(input())
    num_list = list(map(str, input()))

    # 카운트 하는 리스트 생성
    count_list = [0]*10
    for j in num_list:
        count_list[int(j)] += 1
    maxV = maxVid = 0

    # 가장 많은 값 찾기
    for j in range(len(count_list)):
        if count_list[j] >= maxV:
            maxV = count_list[j]
            maxVid = j

    print(f'#{i} {maxVid} {count_list[maxVid]}')