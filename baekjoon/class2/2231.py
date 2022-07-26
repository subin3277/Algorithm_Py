N = int(input())

for i in range(N):
    sum = 0
    for j in str(i) :
        sum += int(j)
    if sum+i == N :
        print(i)
        break
else :
    print(0)
    