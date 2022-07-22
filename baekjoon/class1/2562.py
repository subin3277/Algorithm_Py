my_list = []
for i in range(9) :
    num = int(input())
    my_list.append(num)

max = max(my_list)
print(max)
print(my_list.index(max)+1)