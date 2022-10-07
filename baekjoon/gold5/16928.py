# 뱀과 사다리 게임
from collections import deque

def dfs(v, k): # 정답xxxxxxx
    global res
    if v >= 100:
        if visited[100]:
            lst[100] = min(lst[100], k)
        else:
            lst[100] = k
        return

    visited[v] = True
    for i in range(1, 7):
        t = v + i
        t = min(t, 100)
        if not visited[t]:
            if not (t in snake):
                lst[t] = k + 1
                dfs(t, lst[t])
            if t in ladder:
                lst[ladder[t]] = k + 1
                dfs(ladder[t], lst[t])
        else:
            if not (t in snake):
                lst[t] = min(lst[t], k + 1)
                dfs(t, lst[t])
            if v + i in ladder:
                lst[ladder[t]] = min(lst[t], k + 1)
                dfs(ladder[t], lst[t])

def bfs(): # 정답 oooo
    queue = deque()
    queue.append(1)
    while queue:
        t = queue.popleft()
        for i in range(1, 7):
            nextv = t + i
            if 0 < nextv <= 100 and not visited[nextv]:
                if nextv in ladder.keys():
                    nextv = ladder[nextv]
                elif nextv in snake.keys():
                    nextv = snake[nextv]

                if not visited[nextv]:
                    queue.append(nextv)
                    visited[nextv] = True
                    lst[nextv] = lst[t] + 1

N, M = map(int, input().split())
ladder = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
ladder = dict(sorted(ladder.items()))

snake = {}
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
snake = dict(sorted(snake.items()))

visited = [False] * 101
lst = [0] * 101
bfs()
print(lst[100])
