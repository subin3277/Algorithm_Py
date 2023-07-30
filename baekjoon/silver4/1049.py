# 기타줄

N, M = map(int, input().split())
Set = N // 6
One = N % 6
ans = 0
set_min = 1000
one_min = 1000
for _ in range(M):
    A, B = map(int, input().split())
    set_min = min(set_min, A)
    one_min = min(one_min, B)
ans = set_min * Set + min(one_min * One, set_min)
print(min(ans, N * one_min))