# 스타트와 링크
from itertools import combinations

N = int(input())
num = []
for _ in range(N):
    num.append(list(map(int, input().split())))
people = []
for i in range(1, N+1):
    people.append(i)

for c in combinations(people, N//2):
    print(c)