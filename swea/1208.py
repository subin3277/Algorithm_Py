T = 10
for i in range(1,T+1) :
    width = 100
    N = int(input())
    box_list = list(map(int,input().split()))

    for j in range(N) :
        # 가장 높은 곳에서 꺼내기
        box_list[box_list.index(max(box_list))] -= 1
        # 가장 낮은 곳에 넣기
        box_list[box_list.index(min(box_list))] += 1
    # 옮긴 후 차이 구하기
    res = box_list[box_list.index(max(box_list))] - box_list[box_list.index(min(box_list))]
    
    print(f'#{i} {res}')