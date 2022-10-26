# 색종이

N = int(input())

square = [[0]*101 for _ in range(101)]

for _ in range(N):
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            square[i][j] = 1

ans = 0
for i in square:
    ans += sum(i)
print(ans)
