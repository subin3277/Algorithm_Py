# N과 M 8
from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for c in combinations_with_replacement(lst, M):
    print(*c)