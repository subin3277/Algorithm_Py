import sys
sys.stdin = open("input.txt", "r")

T = 10
for i in range(1,T+1) :
    width = 100
    N = int(input())
    box_list = list(map(int,input().split()))

    for j in range(N) :
        #  최대 최소값 찾기
        maxV = 1
        minV = 100
        for k in box_list:
            if k >= maxV :
                maxV = k
            if k <= minV :
                minV = k
        if maxV-minV == 0 or maxV-minV==1:
            break
        # 가장 높은 곳에서 꺼내기
        box_list[box_list.index(maxV)] -= 1
        # 가장 낮은 곳에 넣기
        box_list[box_list.index(minV)] += 1
    # 옮긴 후 차이 구하기
    maxV = 1
    minV = 100
    for k in box_list:
        if k >= maxV:
            maxV = k
        if k <= minV:
            minV = k
    res = maxV - minV
    
    print(f'#{i} {res}')