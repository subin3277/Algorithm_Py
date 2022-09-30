# 뱀과 사다리 게임

N, M = map(int, input().split())
ladder = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
ladder = dict(sorted(ladder.items()))

snake = {}
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
snake = dict(sorted(snake.items()))
loca = 1
ans = 0
while loca != 100:
    ans += 1
    loca += 6
    if loca > 100:
        loca = 100
        break

    tmp = []
    for i in ladder.keys():
        if loca - 6 < i < loca:
            tmp.append(ladder.get(i))
    if tmp:
        loca = max(tmp)
    else:
        while snake.get(loca, -1) != -1:
            loca -= 1
print(ans)

# 해결 xxxxxxxxxxxxxxxxxx