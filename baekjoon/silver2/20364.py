# 부동산 다툼
import sys
N, Q = map(int, input().split())
lst = set()
for _ in range(Q):
    x = int(sys.stdin.readline().rstrip())
    ans = 0
    tmp = x
    while x > 0:
        if x in lst:
            ans = x
        x = x // 2
    if ans == 0:
        lst.add(tmp)

    print(ans)
