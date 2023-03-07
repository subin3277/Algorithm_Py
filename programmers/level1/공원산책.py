# 공원산책

def solution(park, routes):
    answer = []

    tmp = [[0] * len(park[0]) for _ in range(len(park))]
    for route in routes:
        loca, num = map(str, route.split())
        if loca == 'N' :
            pass
        elif loca == 'S' :
            pass
        elif loca == 'W' :
            pass
        else :
            pass
    return answer

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))