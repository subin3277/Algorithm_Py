# 트리의 부모 찾기

N = int(input())
num = [[] for _ in range(N+1)]
res = [-1] * (N+1)
res[1] = 0
stack = []
for i in range(N-1):
    A, B = map(int, input().split())
    num[A].append(B)
    num[B].append(A)
for i in num[1]:
    stack.append([1, i])
    res[i] = 1
while stack:
    t = stack.pop()
    for i in num[t[1]]:
        if res[i] == -1:
            stack.append([t[1], i])
            res[i] = t[1]
for i in range(2, N+1):
    print(res[i])