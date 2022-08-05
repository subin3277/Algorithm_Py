T = int(input())

for i in range(T) :
    N = int(input()) # N*N 입력
    num_list=[]
    for j in range(N) :
        tmp = list(map(int,input().split()))
        num_list.append(tmp)
    
    #90도
    tmp_list_90 = []
    for j in range(N) :
        res=""
        for k in range(N-1,-1,-1) :
            res += str(num_list[k][j])
        tmp_list_90.append(res)

    #180도
    tmp_list_180=[]
    for j in range(N-1,-1,-1) :
        res=""
        for k in range(N-1,-1,-1) :
            res += str(num_list[j][k])
        tmp_list_180.append(res)

    #270도
    tmp_list_270=[]
    for j in range(N-1,-1,-1):
        res=""
        for k in range(N):
            res += str(num_list[k][j])
        tmp_list_270.append(res)
    
    #출력
    print(f'#{i+1}')
    for j in range(N) :
        print(tmp_list_90[j],end=" ")
        print(tmp_list_180[j],end=" ")
        print(tmp_list_270[j])