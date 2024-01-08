# 석유시추
def solution(land):
    answer = 0
    n = len(land) # 5
    m = len(land[0]) # 8 

    visitied = [[False for _ in range(m)] for _ in range(n)]
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    dict = {}

    v = [0, 0, 1, -1]
    w = [1, -1, 0, 0]
    for i in range(n) :
        for j in range(m) :
            if visitied[i][j] :
                continue
            visitied[i][j] = True
            if land[i][j] == 1 :
                queue = [(i, j)]
                key = len(dict) + 1
                dict[key] = 1
                cnt[i][j] = key
                while queue :
                    dx, dy = queue.pop(0)
                    for x in range(4) :
                        ti = dx + v[x]
                        tj = dy + w[x]
                        if 0 <= ti < n and 0 <= tj < m and not visitied[ti][tj] :
                            visitied[ti][tj] = True
                            if land[ti][tj] == 1 :
                                queue.append((ti, tj))
                                dict[key] += 1
                                cnt[ti][tj] = key
    
    cnt_list = [0 for _ in range(m)]

    for i in range(m) :
        oil_list = set()
        for j in range(n) :
            if land[j][i] == 1 and cnt[j][i] not in oil_list:
                oil_list.add(cnt[j][i])
                cnt_list[i] += dict[cnt[j][i]]
    answer = max(cnt_list)
    return answer

land1 = [[1,1,1,0,0],[1,0,0,0,0],[1,0,1,0,0],[1,0,0,0,0],[1,1,1,0,0]]
land2 = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
land3 = [[0, 0, 0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land3))