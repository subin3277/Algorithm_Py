# N과 M 4
from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
for c in combinations_with_replacement(lst, M):
    print(*c)