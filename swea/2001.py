T = int(input()) # 테스트의 개수

for i in range(T) :
    # N, M 입력받기
    N, M = map(int,input().split())
    fly_list = []

    # 2차원 배열 만들기
    for j in range(N) :
        tmp = list(map(int,input().split()))
        fly_list.append(tmp)

    max = 0 # 최대값
    for j in range(N-M+1) :
        for k in range(N-M+1) :
            ressum=0
            for h in range(k,k+M) :
                # 가로 한줄의 합
                ressum += sum(fly_list[h][j:j+M])

            if ressum > max :
                max = ressum

    
    print(f'#{i+1} {max}')