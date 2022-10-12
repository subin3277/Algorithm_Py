# A -> B
from collections import deque

A, B = map(int, input().split())
ans = -1
stack = deque()
stack.append((A, 1))

while stack:
    t, cnt = stack.popleft()
    if t == B:
        ans = cnt
        break
    if t * 2 <= B:
        stack.append((t*2, cnt + 1))
    tmp = t*10 + 1
    if tmp <= B:
        stack.append((tmp, cnt + 1))
print(ans)