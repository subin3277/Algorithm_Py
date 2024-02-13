# 주사위 굴리기

N, M, X, Y, K = map(int, input().split())
map_num = []
for _ in range(N) :
    num = list(map(int, input().split()))
    map_num.append(num)

navi = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
x = X
y = Y

for n in navi :
    nx = x + dx[n]
    ny = y + dy[n]
    if 0 <= nx < N and 0 <= ny < M :
        if n == 1 :
            dice[4], dice[0], dice[2], dice[1] = dice[1], dice[4], dice[0], dice[2]
        elif n == 2 :
            dice[0], dice[2], dice[1], dice[4] = dice[2], dice[1], dice[4], dice[0]
        elif n == 3 :
            dice[2], dice[3], dice[4], dice[5] = dice[3], dice[4], dice[5], dice[2]
        elif n == 4 : 
            dice[2], dice[3], dice[4], dice[5] = dice[5], dice[2], dice[3], dice[4]
        if map_num[nx][ny] == 0:
            map_num[nx][ny] = dice[4]
        else :
            dice[4] = map_num[nx][ny]
            map_num[nx][ny] = 0
    
        print(dice[2])

        x = nx
        y = ny
