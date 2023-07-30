# 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for _ in range(N):
    max_a = max(A)
    min_b = min(B)
    answer += max_a * min_b
    A.pop(A.index(max_a))
    B.pop(B.index(min_b))
print(answer)