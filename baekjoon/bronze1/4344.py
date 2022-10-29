# 평균은 넘겠지

C = int(input())
for _ in range(C):
    N, *lst = map(int, input().split())
    average = sum(lst) / N
    ans = 0
    for i in lst:
        if i > average:
            ans += 1
    ans = ans/N * 100
    print(f"{ans:.3f}%")