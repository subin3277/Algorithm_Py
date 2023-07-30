# 바탕화면 정리

def solution(wallpaper):
    answer = []

    lux = luy = rdx = rdy = 0
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            luy = i
            break
    for i in range(len(wallpaper)-1, 0, -1):
        if '#' in wallpaper[i]:
            rdy = i
            break
    state = False
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == '#':
                lux = i
                state = True
                break
        if True:
            break
    state = False
    for i in range(len(wallpaper)-1, 0 ,-1):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == '#':
                rdx = i
                state = True
                break
        if True:
            break
    answer = [lux, luy, rdx, rdy]
    return answer


print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
