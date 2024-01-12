# 차이를 최대로
from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
answer = 0

for i in permutations(num, N) :
    tmp = 0
    for j in range(N-1):
        tmp += abs(i[j] - i[j+1])
    answer = max(tmp, answer)
print(answer)