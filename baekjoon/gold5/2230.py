# 수 고르기
N, M = map(int, input().split())
num = [int(input()) for _ in range(N)]
num.sort()

i = 0
j = 1
ans = num[-1] - num[0]
while i < N:
    t = num[j] - num[i]
    if M == t :
        ans = M
        break
    elif M < t :
        i += 1
        ans = min(ans, t)
    else :
        if N -1 > j : j += 1
        else : i += 1

print(ans)