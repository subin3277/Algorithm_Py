# 모든 순열
from itertools import permutations

N = int(input())
lst = [i for i in range(1, N+1)]
for p in permutations(lst):
    print(*p)