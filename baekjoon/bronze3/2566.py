# 최댓값

lst = [list(map(int, input().split())) for _ in range(9)]

ans = x = y = -1
for i in range(9):
    if max(lst[i]) >= ans:
        ans = max(ans, max(lst[i]))
        x = i+1
        y = lst[i].index(ans) + 1
print(ans)
print(x, y)
