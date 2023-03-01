# 비밀번호

N, M = map(int, input().split())
lst = list(map(str, input().split()))
ans = 0
for i in range(1, 10**N):
    for j in lst:
        if j not in str(i).zfill(N):
            break
    else:
        ans += 1
print(ans)