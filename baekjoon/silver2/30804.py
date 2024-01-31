# 과일 탕후루
N = int(input())
fruits = list(map(int, input().split()))
answer = 0
end = 0
kind_cnt = 1
dict = {}
for i in range(1, 10) :
    dict[i] = 0
dict[fruits[0]] += 1

for start in range(N) :
    while kind_cnt < 3 and end < N :
        answer = max(answer, end - start + 1)
        end += 1
        if end < N : 
            if dict[fruits[end]] == 0 :
                kind_cnt += 1
            dict[fruits[end]] += 1
    
    if dict[fruits[start]] == 1:
        kind_cnt -= 1
    dict[fruits[start]] -= 1

print(answer)
