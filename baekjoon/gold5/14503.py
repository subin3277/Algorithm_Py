# 로봇청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
route = [list(map(int,input().split())) for _ in range(N)]
clean = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

robot_x = r
robot_y = c
robot_d = d
answer = 1
clean[r][c] = True
    

while True :
    flag = 0

    for _ in range(4):
        robot_d = (robot_d + 3) % 4
        nx = robot_x + dx[robot_d]
        ny = robot_y + dy[robot_d]
        if 0 <= nx < N and 0 <= ny < M and not clean[nx][ny] and route[nx][ny] == 0:
            clean[nx][ny] = True
            answer += 1
            robot_x = nx
            robot_y = ny
            flag = 1
            break
    
    if flag == 0:
        nx = robot_x - dx[robot_d]
        ny = robot_y - dy[robot_d]
        if route[nx][ny] == 1 :
            break
        else :
            robot_x = nx
            robot_y = ny

print(answer)
