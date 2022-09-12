# 인구이동
from collections import deque
N, L, R = map(int, input().split())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

day = 0
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
while True:
    group = deque() # 연합한 좌표들
    queue = deque()
    visit = [[False] * N for _ in range(N)] # 방문 리스트
    for i in range(N):
        for j in range(N):
            tmp = deque()
            if not visit[i][j]:
                visit[i][j] = True
                queue.append([i, j])
                tmp.append([i, j])
            while queue:
                t = queue.popleft()
                for k in range(4): # 상하좌우 확인
                    x = t[0] + dx[k]
                    y = t[1] + dy[k]
                    if 0 <= x < N and 0 <= y < N and not visit[x][y] and L <= abs(people[t[0]][t[1]] - people[x][y]) <= R:
                        queue.append([x, y])
                        tmp.append([x, y])
                        visit[x][y] = True # 방문 표시
            if tmp: # 연합한 곳이 있다면 그룹리스트에 추가
                group.append(tmp)
    if len(group) == N * N:
        break
    day += 1
    for i in group:
        peoplesum = 0 # 각 나라의 인구 더하기
        for j in i:
            peoplesum += people[j[0]][j[1]]
        peoplesum = peoplesum//len(i) # 연합한 나라의 최종 인구수
        for j in i:
            people[j[0]][j[1]] = peoplesum # 인구수 바꾸기

print(day)