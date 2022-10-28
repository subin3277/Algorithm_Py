# 제로
from collections import deque

K = int(input())
stack = deque()
ans = 0
for _ in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)
        ans += N
    else:
        ans -= stack.pop()
print(ans)
