A = int(input())
B = int(input())
C = int(input())
res = str(A*B*C)
count_list = [0,0,0,0,0,0,0,0,0,0]
for i in res :
    count_list[int(i)] += 1
for i in count_list :
    print(i) 