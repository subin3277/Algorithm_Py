# 탈출

R, C = map(int, input().split())
loca = []
for _ in range(R):
    loca.append(list(map(str, input())))
water = []
gosum = []
tmpwater = []
tmpgosum = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(R): # 고슴도치와 물 위치 찾기
    for j in range(C):
        if loca[i][j] == 'S':
            gosum.append([i, j, 0])
        elif loca[i][j] == '*':
            water.append([i, j])
count = 0
state = False
while True:
    count += 1
    tmpwater = water.copy()
    while tmpwater: # 물 퍼지기
        t = tmpwater.pop()
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if 0 <= x < R and 0 <= y < C and loca[x][y] == '.': # 비어있는 곳이면
                loca[x][y] = '*' # 물 움직이기
                water.append([x, y])
    tmpgosum = []
    while gosum: # 고슴도치 움직이기
        t = gosum.pop()
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if 0 <= x < R and 0 <= y < C and loca[x][y] == 'D': # 비버 굴이면
                print(count) # 출력하고 그만
                state = True
                break
            elif 0 <= x < R and 0 <= y < C and loca[x][y] == '.': # 비어있는 곳이면
                loca[x][y] = 's' # 지난곳 표시
                tmpgosum.append([x, y]) # 움직이기
        if state:
            break
    gosum = tmpgosum.copy()

    if state:
        break

    if len(gosum) == 0: # 더이상 갈곳 없으면
        print("KAKTUS")
        break
