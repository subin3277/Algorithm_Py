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

    for route in routes:
        loca, num = map(str, route.split())
        num = int(num)
        if loca == 'N':
            if nowx - num >= 0:
                for i in range(nowx-num, nowx):
                    if park[i][nowy] == 'X':
                        break
                else :
                    nowx = nowx - num
        elif loca == 'S':
            if nowx + num < W:
                for i in range(nowx, nowx+num+1):
                    if park[i][nowy] == 'X':
                        break
                else :
                    nowx = nowx + num
        elif loca == 'W':
            if nowy - num >= 0 and not('X' in park[nowx][nowy-num:nowy]):
                nowy = nowy - num
        else:
            if nowy + num < H and not ('X' in park[nowx][nowy:nowy+num+1]):
                nowy = nowy + num
    answer = [nowx, nowy]
    return answer


# park = ["SOO", "OOO", "OOO"]
# routes = ["E 2", "S 2", "W 1"]
# print(solution(park, routes))

# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2,1]
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0,1]
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0,0]
#
# print(solution(["OSO","OOO","OOO","OOO"], ["W 2"])) # [0,1]
# print(solution(["OSO","OOO","OOO","OOO"], ["N 2"])) # [0,1]
# print(solution(["OSO","OOO","OOO","OOO"], ["S 5"])) # [0,1]
# print(solution(["OSO","OOO","OOO","OOO"], ["E 5"])) # [0,1]

# print(solution(["XXX","XSX","XXX"], ["E 1"])) # [1,1]
# print(solution(["XXX","XSX","XXX"], ["W 1"])) # [1,1]
# print(solution(["XXX","XSX","XXX"], ["S 1"])) # [1,1]
# print(solution(["XXX","XSX","XXX"], ["N 1"])) # [1,1]

# print(solution(["SOXOO","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"])) # [0, 0]
# print(solution(["SOOOX","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"])) # [0, 3]
# print(solution(["XOOOS","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["W 3"])) # [0, 1]
# print(solution(["OOXOS","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["W 3"])) # [0, 4]
# print(solution(["SOOOO","OOOOO","XOOOO", "OOOOO", "OOOOO"], ["S 3"])) # [0, 0]
# print(solution(["SOOOO","OOOOO","OOOOO", "OOOOO", "XOOOO"], ["S 3"])) # [3, 0]
# print(solution(["OOOOO","OOOOO","XOOOO", "OOOOO", "SOOOO"], ["N 3"])) # [4, 0]
print(solution(["XOOOO","OOOOO","OOOOO", "OOOOO", "SOOOO"], ["N 3"])) # [1, 0]