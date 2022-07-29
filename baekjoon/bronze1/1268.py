N = int(input())

class_list= []
same = [0] * N
for i in range(N) :
    tmp = list(map(int,input().split()))
    class_list.append(tmp)
    same[i] = [0]*N




for i in range(5):
    for j in range(N) :
        for k in range(j+1,N) :
            if class_list[j][i] == class_list[k][i] :
                same[k][j] = 1
                same[j][k] = 1

count = []
for i in same :
    count.append(i.count(1))
print(count.index(max(count))+1)