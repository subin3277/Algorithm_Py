# 팩토리얼 0의 개수
N = int(input())

ans = 0
while N > 0:
    ans += N//5
    N //= 5
print(ans)