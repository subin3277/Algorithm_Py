# N과 M 9
from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
for p in permutations(lst, M):
    ans.append(p)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(*i)