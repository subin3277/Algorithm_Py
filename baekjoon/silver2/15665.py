# N과 M(11)
from itertools import product

N, M = map(int, input().split())
num = sorted(list(set(list(map(int, input().split())))))
for i in product(num, repeat = M) :
    print(*i)