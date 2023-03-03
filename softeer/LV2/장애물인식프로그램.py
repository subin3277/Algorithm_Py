# 장애물 인식 프로그램

N = int(input())
maps = [list(map(str, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if visited[i][j] or maps[i][j] == '0':
            continue
        visited[i][j] = True
        queue = [[i, j]]
        cnt = 1
        while queue:
            tx, ty = queue.pop(0)
            for k in range(4):
                x = tx + dx[k]
                y = ty + dy[k]
                if 0 <= x < N and 0 <= y < N and not visited[x][y] and maps[x][y] == '1':
                    visited[x][y] = True
                    queue.append([x, y])
                    cnt += 1
        ans.append(cnt)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
