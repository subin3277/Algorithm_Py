# 터렛

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    x = x1 - x2
    y = y1 - y2
    d = (abs(x) ** 2 + abs(y) ** 2) ** 0.5

    if d == 0 :
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r1 + r2 < d or abs(r1-r2) > d:
        print(0)
    elif r1+r2 == d or abs(r1-r2) == d:
        print(1)
    else:
        print(2)