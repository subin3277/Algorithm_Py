# 색종이 만들기

def sol(x, y, N):
    global blue, white
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                sol(x, y, N//2)
                sol(x+N//2, y, N//2)
                sol(x, y+N//2, N//2)
                sol(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
blue = white = 0
sol(0, 0, N)
print(white)
print(blue)
