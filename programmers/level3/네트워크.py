from collections import deque
check = set([0])

def bfs(i, computers, n):
    global check
    dq = deque()
    dq.append(i)
    while dq:
        pop = dq.popleft()
        for j in range(n):
            if computers[pop][j]==1 and pop!=j and j not in check:
                dq.append(j)
                check.add(j)
    return

def solution(n, computers):
    global check
    answer = 0
    bfs(0,computers,n)
    answer += 1
    while len(check)!=n:
        for i in range(n):
            if i not in check:
                check.add(i)
                bfs(i,computers,n)
                answer+=1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] ))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] ))