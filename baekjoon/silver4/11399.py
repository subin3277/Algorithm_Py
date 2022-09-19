# ATM

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = sum(lst) * N
for i in range(len(lst)-1, 0, -1):
    ans -= lst[i] * i
print(ans)