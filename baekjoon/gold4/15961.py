# 회전 초밥
N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

start = -K
end = -1
sushi_set = set(sushi[start::])
answer = 0

while end < N - 1 :
    sushi_set.remove(sushi[start])
    if sushi[end] in sushi_set :
        sushi_set.remove(sushi[end])
    start += 1
    if start == N :
        start = 0
    end += 1
    
    sushi_set.add(sushi[start])
    sushi_set.add(sushi[end])
    if C in sushi_set :
        answer = max(answer, len(sushi_set))
    else :
        answer = max(answer, len(sushi_set) + 1)

print(answer)
