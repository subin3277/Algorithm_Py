# 설탕 배달

N = int(input())

ans = N
for i in range(N//5, -1, -1):
    if (N - i*5) % 3 == 0:
        ans = min((N-i*5)//3 + i, ans)
        break
else:
    ans = -1
print(ans)