T = int(input())

for i in range(T) : 
    input_list = list(map(int,input().split()))
    sum = 0
    for j in input_list :
        if j%2 != 0 :
            sum += j
    print(f'#{i+1} {sum}')