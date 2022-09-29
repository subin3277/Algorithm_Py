# 그룹 나누기
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def solution(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        t = queue.popleft()
        for i in node[t]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    node = [[] for _ in range(N + 1)]
    for i in range(M):
        node[num_list[i*2]].append(num_list[i*2+1])
        node[num_list[i*2+1]].append(num_list[i*2])
    visited = [False] * (N+1)
    ans = 0
    for i in range(1, N + 1):
        if not visited[i]:
            solution(i)
            ans += 1
    print(f'#{test} {ans}')
