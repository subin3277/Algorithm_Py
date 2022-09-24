
from itertools import product
def solution(n, m, x, y, r, c, k):
    answer = ''
    miro = [[0] * m for _ in range(n)]
    miro[x-1][y-1] = 1 # 출발
    miro[r-1][c-1] = 2 # 도착

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    d = ['d', 'l', 'r', 'u']
    res = []
    for p in product(d, repeat=k):
        print(p)
        x1 = x-1
        y1 = y-1
        for i in p:
            t = d.index(i)
            x1 += dx[t]
            y1 += dy[t]
            if not (0 <= x1 < n and 0 <= y1 < m):
                break
        else:
            if miro[x1][y1] == 2:
                res = p
                pass
    if len(res) == 0:
        answer = "impossible"
    else:
        for i in res:
            answer += i
    return answer

n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5
print(solution(n, m, x, y, r, c, k))