# 나의 인생에는 수학과 함께

N = int(input())
route = [list(map(str, input().split())) for _ in range(N)]

max_res = -(5**20)
min_res = 5 ** 20

def DFS(x, y, res, cal) :
    global max_res, min_res
    if x == N-1 and y == N-1 :
        max_res = max(max_res, int(eval(res+cal+route[x][y])))
        min_res = min(min_res, int(eval(res+cal+route[x][y])))
        return
    elif x >= N or y >= N:
        return
    
    if route[x][y].isdecimal() :
        DFS(x+1, y, str(eval(res+cal+route[x][y])), cal)
        DFS(x, y+1, str(eval(res+cal+route[x][y])), cal)
    else :
        DFS(x+1, y, res, route[x][y])
        DFS(x, y+1, res, route[x][y])

DFS(0, 0, '0', '+')
print(max_res, min_res)