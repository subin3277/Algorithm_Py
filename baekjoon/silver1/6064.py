# 카잉 달력

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    ans = -1
    i = 0
    while x <= M*N:
        if x%N == y%N:
            ans = x
            break
        x += M
    print(ans)