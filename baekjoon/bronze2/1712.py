# 손익분기점

A, B, C = map(int, input().split())

if C-B <=0 :
    print(-1)
else:
    res = A // (C-B)
    print(res + 1)