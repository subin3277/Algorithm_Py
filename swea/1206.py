T = 10
for i in range(1,T+1) :
    len = int(input())
    building = list(map(int,input().split()))
    res = 0
    for j in range(2,len-2) :
        # 탐색할 빌딩의 층이 가장 높을 때(양옆2개보다 낮으면 조망권 확보x)
        if max(building[j-2:j+3]) == building[j] :
            # 양옆에 있는 빌딩들 중 가장 높은 층을 알아내기
            tmpmax = max(building[j-2],building[j-1],building[j+1],building[j+2])
            # 기준 층과 옆중 높은 빌딩의 층을 빼면 조망권 있는 층수 알수 있다.
            res += building[j]-tmpmax

    print(f'#{i} {res}')