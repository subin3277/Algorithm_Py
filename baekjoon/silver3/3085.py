# 사탕게임

N = int(input())
candy = []
for i in range(N):
    candy.append(list(map(str, input())))
# 빨강: C 파랑: P 초록: Z 노랑: Y
maxcandy = N
while True:

# 교환 안하고 찾기
    res = False
    for i in range(N):
        for j in range(N - maxcandy + 1): # 행에서 찾기
            if candy[i][j:j+maxcandy] == ['C'] * maxcandy or candy[i][j:j+maxcandy] == ['P'] * maxcandy or candy[i][j:j+maxcandy] == ['Z'] * maxcandy or candy[i][j:j+maxcandy] == ['Y'] * maxcandy:
                res = True
                break
            tmp = []
            for k in range(j, j + maxcandy): # 열에서 찾기
                tmp.append(candy[k][i])
            if tmp == ['C'] * maxcandy or tmp == ['P'] * maxcandy or tmp == ['Z'] * maxcandy or tmp == ['Y'] * maxcandy:
                res = True
                break
        if res: break
    if res: break
    # 교환할 곳 찾기

    for i in range(N):
        for j in range(N - maxcandy + 1):
            tmp = []
            colorcount = { 'C' : 0, 'P' : 0, 'Z' : 0, 'Y' : 0}
            for k in range(j, j + maxcandy):
                tmp.append(candy[i][k])
                colorcount[candy[i][k]] += 1
            if maxcandy-1 in colorcount.values(): # 한개만 다른 곳 찾기
                for x, y in colorcount.items():
                    if y == 1:
                        switchstr = x # 하나만 다른 str
                    if y == maxcandy - 1:
                        moststr = x
            else : break
            switchidx = tmp.index(switchstr) + j
            if (i >= 0 and candy[i-1][switchidx] == moststr) or (i < N-1 and candy[i+1][switchidx] == moststr):
                res = True
                break
        if res: break
    if res: break
    for i in range(N):
        for j in range(N - maxcandy + 1):
            tmp = []
            colorcount = { 'C' : 0, 'P' : 0, 'Z' : 0, 'Y' : 0}
            for k in range(j, j + maxcandy):
                tmp.append(candy[k][i])
                colorcount[candy[k][i]] += 1
            if maxcandy-1 in colorcount.values(): # 한개만 다른 곳 찾기
                for x, y in colorcount.items():
                    if y == 1:
                        switchstr = x # 하나만 다른 str
                    if y == maxcandy - 1:
                        moststr = x
            else: break
            switchidx = tmp.index(switchstr) + j
            if (i >= 0 and candy[switchidx][i - 1] == moststr) or (i < N-1 and candy[switchidx][i + 1] == moststr):
                res = True
                break
        if res: break
    if res: break
    maxcandy -= 1

print(maxcandy)
