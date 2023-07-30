# 금고털이

W, N = map(int, input().split())
juwel = [list(map(int, input().split())) for _ in range(N)]

juwel.sort(key=lambda x: x[1], reverse=True)
weight = 0
ans = 0
for i in juwel:
    if weight + i[0] <= W:
        weight += i[0]
        ans += i[0] * i[1]
    else:
        ans += (W - weight) * i[1]
        break
print(ans)
