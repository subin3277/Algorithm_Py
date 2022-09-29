# 최소비용
import sys
sys.stdin = open("input.txt", "r")

def bfs(si, sj):
    q = []
    s = [[100000] * N for _ in range(N)]

    q.append((si, sj))
    s[si][sj] = 0  # 0이 아니라 arr[si][sj]인 경우도 있음

    while q:
        ci, cj = q.pop(0)  # 중복방문가능 -> q empty일 때까지 작동
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and s[ni][nj] > s[ci][cj] + 1 + max(0, num[ni][nj] - num[ci][cj]):
                s[ni][nj] = s[ci][cj] + 1 + max(0, num[ni][nj] - num[ci][cj])
                q.append((ni, nj))

    return s[N - 1][N - 1]

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(0, 0)
    print(f'#{test} {ans}')