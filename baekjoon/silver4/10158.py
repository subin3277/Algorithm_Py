# 개미
import sys
sys.stdin = open("input.txt", "r")

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dx = [1, -1, 1, -1] # 오른쪽 아래, 왼쪽 아래, 오른쪽 위, 왼쪽 위,
dy = [1, 1, -1, -1]
k = 0
for i in range(t):
    p += dx[k]
    q += dy[k]
    if ((p == w or p == 0) and (q == 0 or q == h)) or p == 0: # 꼭짓점과 만나거나, p가 0과 만나면
        k = (3 - k) % 4
    elif q == 0: # q가 0과 만나면
        k = (k+2) % 4
    elif p == w: # p가 최대 가로를 만나면
        k = (k+1) % 4
    elif q == h: # q가 최대 세로를 만나면
        k = (k-2) % 4
print(p, q)
# xxxxxxxxxx해결xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx