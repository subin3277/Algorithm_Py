# 이중 우선순위 큐
import sys, heapq

T = int(input())
for test in range(1, T+1):
    K = int(input())
    Q_max = []
    Q_min = []
    visited = [False] * K
    for i in range(K):
        A, B = map(str, sys.stdin.readline().split())
        if A == 'I':
            heapq.heappush(Q_min, (int(B), i))
            heapq.heappush(Q_max, (int(B) * (-1), i))
            visited[i] = True
        else:
            if B == "1":
                while Q_max and not visited[Q_max[0][1]]:
                    heapq.heappop(Q_max)
                if Q_max:
                    data, idx = heapq.heappop(Q_max)
                    visited[idx] = False
            else:
                while Q_min and not visited[Q_min[0][1]]:
                    heapq.heappop(Q_min)
                if Q_min:
                    data, idx = heapq.heappop(Q_min)
                    visited[idx] = False

    while Q_min and not visited[Q_min[0][1]]:
        heapq.heappop(Q_min)
    while Q_max and not visited[Q_max[0][1]]:
        heapq.heappop(Q_max)

    if Q_max and Q_min:
        print(-Q_max[0][0], Q_min[0][0])
    else:
        print("EMPTY")