# 동전 0

N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

res = 0
i = len(money) - 1
while K != 0:
    if K // money[i] > 0:
        res += K // money[i]
        K = K % money[i]
    i -= 1
print(res)