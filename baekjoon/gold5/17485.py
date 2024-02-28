# 진우의 달 여행

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
res = [[[-1, -1, -1] for _ in range(M)] for _ in range(N)]

dy = [-1, 0 ,1]

for i in range(M):
    res[0][i] = [space[0][i]] * 3

for i in range(1, N) :
    for j in range(M) :
        for k in range(3) :
            nx = i - 1
            ny = j + dy[k]
            if 0 <= ny < M:
                if res[nx][ny][(k+2)%3] == -1 :
                    res[i][j][k] = res[nx][ny][(k+1)%3] + space[i][j]
                elif res[nx][ny][(k+1)%3] == -1 :
                    res[i][j][k] = res[nx][ny][(k+2)%3] + space[i][j]
                else:
                    res[i][j][k] = min(res[nx][ny][(k+2)%3] + space[i][j] , res[nx][ny][(k+1)%3] + space[i][j])

res = sum(res[-1], [])
print(min(res[1 : len(res) - 1]))