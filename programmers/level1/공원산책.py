# 공원산책

def solution(park, routes):
    answer = []

    W = len(park)
    H = len(park[0])

    nowx = nowy = 0
    for i in range(len(park)):
        if 'S' in park[i]:
            nowx = i
            nowy = park[i].find('S')

    tmp = [[0] * len(park[0]) for _ in range(len(park))]
    for route in routes:
        loca, num = map(str, route.split())
        num = int(num)
        if loca == 'N':
            if nowx - num >= 0:
                nowx = nowx - num
        elif loca == 'S':
            if nowx + num < W:
                nowx = nowx + num
        elif loca == 'W':
            if nowy - num >= 0:
                nowy = nowy - num
        else:
            if nowy + num < H:
                nowy = nowy + num
    answer = [nowx, nowy]
    return answer


park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))
