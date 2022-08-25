# 카드 섞기
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
cycle = [0, 1, 2] * (N//3)
card = [0, 1, 2] * (N//3)
count = 0
P2 = [[] for _ in range(3)]
res = []
for i in range(N):
    P2[P[i]].append(i % 3)
for i in range(N//3):
    for j in range(3):
        res.append(P2[j][i])
print(res)
while True:
    initcard = card.copy()
    if res == card:
        break

    for i in range(N):
        card[S[i]] = initcard[i]
    count += 1

    if count == 59:
        print(card)
        break
    if card == cycle:
        print(count)
        count = -1
        break


print(count)

# 해결xxxxxxxxxxxxxxxxx