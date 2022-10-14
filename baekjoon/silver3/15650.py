# N과 M
from itertools import combinations

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
for p in combinations(lst, M):
    print(*p)

    ###