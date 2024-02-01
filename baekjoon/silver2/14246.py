# K보다 큰 구간
N = int(input())
num = list(map(int, input().split()))
K = int(input())

answer = 0
end = 0
sum = num[0]

for start in range(N) :
    while sum <= K and end < N :
        end += 1
        if end < N :
            sum += num[end]

    if sum > K :
        answer += (N - end)
    
    sum -= num[start]

print(answer)