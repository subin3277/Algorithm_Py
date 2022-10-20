# 체스판 다시 칠하기

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(str, input())))

res = 32
for i in range(N-7):
    for j in range(M-7):
        first = lst[i][j]
        count = 0

        for x in range(8):
            for y in range(8):
                if lst[i+x][j+y] != first:
                    count += 1
                if first == 'W':
                    first = 'B'
                else:
                    first = 'W'
            if first == 'W':
                first = 'B'
            else:
                first = 'W'
        count = min(count, 64-count)
        res = min(res, count)
print(res)