# 어린왕자

T = int(input()) # 테스트 케이스
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) # 출발지 , 도착지

    N = int(input()) # 행성 갯수
    ans = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split()) # 행성 중심, 반지름
        a = (abs(x1-cx)**2 + abs(y1-cy)**2)**(1/2)
        b = (abs(x2-cx)**2 + abs(y2-cy)**2)**(1/2)
        if (a < r and b > r) or (a > r and b < r):
            ans += 1
    print(ans)
