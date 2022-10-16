# 가장 긴 증가하는 부분 수열

N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N
ans[-1] = 1
for i in range(N - 2, -1, -1):
    tmp = [0]
    for j in range(i+1, N):
        if lst[i] < lst[j]:
            tmp.append(ans[j])
    ans[i] = max(tmp) + 1
print(max(ans))