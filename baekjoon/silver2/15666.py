# N과 M 12
from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = list(set(map(int, input().split())))
lst.sort()
for c in combinations_with_replacement(lst, M):
    print(*c)