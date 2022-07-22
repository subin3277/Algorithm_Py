N = int(input())
sc_list = list(map(int,input().split()))

max = max(sc_list)

for i in range(N) :
    sc_list[i] = sc_list[i]/max*100
    
print(sum(sc_list)/N)