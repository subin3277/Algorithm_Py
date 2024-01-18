# 진우의 민트초코우유
N, M, H = map(int, input().split())
loca = [[] for _ in range(N)]
home = [0, 0]
milk_list = []
for i in range(N) :
    loca[i] = list(map(int, input().split()))
    for j in range(N) :
        if loca[i][j] == 2:
            milk_list.append([i, j])
        elif loca[i][j] == 1:
            home = [i, j]

visited = [False] * len(milk_list)
answer = 0

def Move(nx, ny, hp, milk) :
    global answer

    if hp == 0:
        return
    
    for i in range(len(milk_list)) :
        if not visited[i] :
            dist = abs(nx - milk_list[i][0]) + abs(ny - milk_list[i][1])
            if dist <= hp :
                visited[i] = True
                Move(milk_list[i][0], milk_list[i][1], hp - dist + H, milk + 1)
                visited[i] = False

    if hp >= abs(home[0] - nx) + abs(home[1] - ny) :
        answer = max(answer, milk)

Move(home[0], home[1], M, 0)
print(answer)