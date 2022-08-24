# 카드 섞기
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
cycle = [0, 1, 2] * (N//3)
card = [0, 1, 2] * (N//3)
count = 0
P2 = [0] * N
for i in range(N):
    P2[i] = P[i]
while True:
    initcard = card.copy()
    if card == [0,0,2,2,1,1,1,0,0,2,1,2]:
        break

    for i in range(N):
        card[S[i]] = initcard[i]
    count += 1

    if card == cycle:
        count = -1
        break


print(count)

# 해결xxxxxxxxxxxxxxxxx