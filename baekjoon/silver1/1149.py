# RGB거리
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in range(1, N):
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    lst[i][1] += min(lst[i - 1][0], lst[i - 1][2])
    lst[i][2] += min(lst[i - 1][1], lst[i - 1][0])
print(min(lst[N-1][0], lst[N-1][1], lst[N-1][2]))

