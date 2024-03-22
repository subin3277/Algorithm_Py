# 가장 가까운 세사람의 심리적 거리
from itertools import combinations

T = int(input())
for _ in range(T) :
    N = int(input())
    people = list(map(str, input().split()))

    ans = 12

    if N <= 16 :
        for A, B, C in combinations(people, 3) :
            a = set(A)
            b = set(B)
            c = set(C)
            tmp = len(a-b) + len(a-c) + len(b-c)
            ans = min(tmp, ans)
    else :
        dict={}
        for i in people:
            dict[i] = dict.get(i, 0) + 1
            if dict[i] >= 3 :
                ans = 0
                break
        
        if ans != 0 :
            ans = 2

    print(ans)