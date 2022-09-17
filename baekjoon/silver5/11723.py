# 집합
import sys
M = int(input())
S = set()
for _ in range(M):
    lst = sys.stdin.readline().split()

    todo = lst[0]
    if len(lst) == 2 :
        lst[1]  = int(lst[1])
    if todo == 'add':
        S.add(lst[1])
    elif todo == 'remove':
        if lst[1] in S:
            S.discard(lst[1])
    elif todo == 'check':
        if not (lst[1] in S):
            print(0)
        else:
            print(1)
    elif todo == 'toggle':
        if not lst[1] in S:
            S.add(lst[1])
        else:
            S.discard(lst[1])
    elif todo == 'all':
        S = set([i for i in range(1, 21)])
    elif todo == 'empty':
        S = set()