# DSLR
from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    stack = deque()
    stack.append((A, ""))
    visited = set()
    visited.add(A)

    while stack:
        t = stack.popleft()
        if t[0] == B:
            print(t[1])
            break

        tmp = (t[0] * 2) % 10000
        if tmp not in visited:
            visited.add(tmp)
            stack.append((tmp, t[1] + "D"))

        tmp = t[0] - 1
        if tmp == -1:
            tmp = 9999
        if tmp not in visited:
            visited.add(tmp)
            stack.append((tmp, t[1] + "S"))

        tmp = t[0] // 1000 + (t[0] % 1000) * 10
        if tmp not in visited:
            visited.add(tmp)
            stack.append((tmp, t[1] + "L"))

        tmp = (t[0] % 10) * 1000 + t[0] // 10
        if tmp not in visited:
            visited.add(tmp)
            stack.append((tmp, t[1] + "R"))
