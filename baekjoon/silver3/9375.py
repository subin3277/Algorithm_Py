# 패션왕 신해빈
T = int(input())
for test in range(T):
    N = int(input())
    dict = {}
    for _ in range(N):
        A, B = map(str, input().split())
        if B in dict:
            dict[B].append(A)
        else:
            dict[B] = [A]
    res = 1
    for i in dict.values():
        res *= len(i) + 1
    print(res - 1)