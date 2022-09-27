# 전기버스2
import sys
sys.stdin = open("input.txt", "r")

def dfs(n, cnt, sm):
    global ans
    if ans <= cnt:
        return

    if n == N:
        ans = min(ans, cnt)
        return
    if sm > 0:
        dfs(n+1, cnt, sm-1)
    dfs(n+1, cnt+1, tmp[n]-1)

T = int(input())
for test in range(1, T + 1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = tmp[1:]
    ans = N
    dfs(2, 0, tmp[1] - 1)
    print(f'#{test} {ans}')
