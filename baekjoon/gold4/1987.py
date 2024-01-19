# 알파벳
import sys
R, C = map(int, sys.stdin.readline().split())

alphabet = [list(map(str, sys.stdin.readline())) for _ in range(R)]
answer = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [False] * 26
visited[ord(alphabet[0][0]) - 65] = True

def BT(x, y, count) :
    global answer
    answer = max(answer, count)

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[ord(alphabet[nx][ny]) - 65] :
                visited[ord(alphabet[nx][ny]) - 65] = True
                BT(nx, ny, count + 1)
                visited[ord(alphabet[nx][ny]) - 65] = False

BT(0, 0, 1)
print(answer)