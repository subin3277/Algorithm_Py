N, M = map(int,input().split())
card = list(map(int,input().split()))
card.sort()

res = 0
for i in range(N-2) :
    for j in range(i+1,N-1) :
        for k in range(j+1,N) :
            sum = card[i]+card[k]+card[j]
            if sum <= M and sum > res :
                res = sum
                break
            elif sum > M :
                break
print(res)