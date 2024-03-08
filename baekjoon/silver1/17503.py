# 맥주 축제
import heapq

N, M, K = map(int, input().split())
beer = [list(map(int, input().split())) for _ in range(K)]
ans = -1
drink = []

# 도수 기준으로 정렬
beer.sort(key=lambda x:x[1])
fav = 0
for i in beer :
    if len(drink) < N:
        heapq.heappush(drink, i)
        fav += i[0]
        if len(drink) == N:
            if fav >= M :
                ans = i[1]
                break
            else:
                fav -= heapq.heappop(drink)[0]

print(ans)