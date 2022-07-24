T = int(input())

for i in range(T) : 
    input_list = list(map(int,input().split()))
    sum = 0
    for j in input_list :
        sum += j
    aver = round(sum/10)
    print(f'#{i+1} {aver}')