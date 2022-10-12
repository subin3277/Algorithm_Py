# 테트로미노
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, c, k):
    global ans
    if ans >= k + max_value*(3-c):
        return
    if c == 3:
        ans = max(ans, k)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if c == 1:
                visited[nx][ny] = True
                dfs(x, y, c + 1, k + lst[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, c + 1, k + lst[nx][ny])
            visited[nx][ny] = False

def dfs2(x, y):
    global ans
    for i in range(4):
        tmp = lst[x][y]
        for k in range(3):
            t = (i+k)%4
            nx = x + dx[t]
            ny = y + dy[t]

            if not (0 <= nx < N and 0 <= ny < M):
                tmp = 0
                break
            tmp += lst[nx][ny]
        ans = max(ans, tmp)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_value = max(map(max, lst))

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, lst[i][j])
        visited[i][j] = False

print(ans)