from itertools import count


my_list = list(map(int,input().split()))

n = min(my_list)
while True :
    count = 0
    for i in range(5) :
        if n % my_list[i] == 0 :
            count +=1
    if count >= 3 :
        print(n)
        break
    else :
        n += 1