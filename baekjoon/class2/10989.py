

""" sort_list = []
for i in range(N) :
    num = int(input())
    sort_list.append(num)
sort_list.sort()
for i in sort_list:
    print(i) """
N = int(input())
sort_list = [0]*N
for i in range(N) :
    num = int(input())
    sort_list[num] += 1
    

for i in range(1,N):
    while (sort_list[i]>0) :
        print(i)
        sort_list[i]-=1