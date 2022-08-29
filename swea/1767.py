# 프로세서 연결하기
T = int(input())
for test in range(1, T+1):
    N = int(input())
    core_list = []
    for _ in range(N):
        core_list.append(list(map(int, input().split())))
    minres = N * N + 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    core_loca = []
    tmp_list = core_list.copy()
    res = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if tmp_list[i][j] == 1:
                core_loca.append([i, j])

    dict_count = [[] for _ in range(len(core_loca))]
    for j in range(len(core_loca)):
        for i in range(4):
            nxtx = core_loca[j][0] + dx[i]
            nxty = core_loca[j][1] + dy[i]
            count = 0
            while 0 <= nxtx < N and 0 <= nxty < N and tmp_list[nxtx][nxty] != 1:
                nxtx += dx[i]
                nxty += dy[i]
                count += 1
            if not(0 <= nxtx < N and 0 <= nxty < N):
                dict_count[j].append(count)


    while dict_count:
        if dict_count == [[]]:
            break
        minlen = 4
        minidx = -1
        for i in range(len(dict_count)):
            if 0 < len(dict_count[i]) <= minlen:
                minlen = len(dict_count[i])
                minidx = i
        minpos = minidx
        if minlen == 1:
            for i in range(4):
                stack = [[core_loca[minpos][0], core_loca[minpos][1]]]
                nxtx = core_loca[minpos][0] + dx[i]
                nxty = core_loca[minpos][1] + dy[i]
                while 0 <= nxtx < N and 0 <= nxty < N and tmp_list[nxtx][nxty] != 1:
                    stack.append([nxtx, nxty])
                    nxtx += dx[i]
                    nxty += dy[i]
                if not(0 <= nxtx < N and 0 <= nxty < N):
                    res += len(stack) - 1
                    stack.pop(0)
                    while stack:
                        t= stack.pop()
                        tmp_list[t[0]][t[1]] = -1
                    dict_count.remove(dict_count[minpos])
                    core_loca.remove([core_loca[minpos][0], core_loca[minpos][1]])
                    break
        else:
            mintmp = min(dict_count[minpos])
            for i in range(4):
                stack = [[core_loca[minpos][0], core_loca[minpos][1]]]
                nxtx = core_loca[minpos][0] + dx[i]
                nxty = core_loca[minpos][1] + dy[i]
                tmpcnt = 0
                while 0 <= nxtx < N and 0 <= nxty < N and tmp_list[nxtx][nxty] != 1:
                    stack.append([nxtx, nxty])
                    nxtx += dx[i]
                    nxty += dy[i]
                    tmpcnt += 1
                if not(0 <= nxtx < N and 0 <= nxty < N) and tmpcnt == mintmp:
                    res += len(stack) - 1
                    stack.pop(0)
                    while stack:
                        t= stack.pop()
                        tmp_list[t[0]][t[1]] = -1
                    dict_count.remove(dict_count[minpos])
                    core_loca.remove([core_loca[minpos][0], core_loca[minpos][1]])
                    break

        dict_count = [[] for _ in range(len(core_loca))]
        for j in range(len(core_loca)):
            for i in range(4):
                nxtx = core_loca[j][0] + dx[i]
                nxty = core_loca[j][1] + dy[i]
                count = 0
                while 0 <= nxtx < N and 0 <= nxty < N and tmp_list[nxtx][nxty] != 1 and tmp_list[nxtx][nxty] != -1:
                    nxtx += dx[i]
                    nxty += dy[i]
                    count += 1
                if not (0 <= nxtx < N and 0 <= nxty < N):
                    dict_count[j].append(count)

    print(f'#{test} {res}')
    # 해결xxxxxxxxxxxxxxxxxxxxxxxxxx