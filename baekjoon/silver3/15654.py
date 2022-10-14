# N과 M 5
from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for p in permutations(lst, M):
    print(*p)