# 꽃길

N = int(input())
flower = [list(map(int, input().split())) for _ in range(N)]
price = [[-1] * N for _ in range(N)]
loca = []

for i in range(N) :
    for j in range(N) :
        if 0 < i < N - 1 and 0 < j < N-1 :
            price[i][j] = flower[i][j] + flower[i-1][j] + flower[i+1][j] + flower[i][j+1] + flower[i][j-1]
            loca.append([price[i][j], i , j])

loca.sort()
answer = 200 * 5 * 3
sum = 0

def check(x1, y1, x2, y2, x3, y3):
    if abs(x1 - x2) + abs(y1 - y2) < 3 :
        return False
    if abs(x2 - x3) + abs(y2 - y3) < 3 :
        return False
    if abs(x1- x3) + abs(y1- y3) < 3:
        return False
    return True

for i in range(len(loca)):
    if loca[i][0] >= answer : break
    for j in range(i+1, len(loca)) :
        if loca[i][0] + loca[j][0] >= answer :break
        for k in range(j+1, len(loca)) :
            sum = loca[i][0] + loca[j][0] + loca[k][0]
            if sum >= answer :
                break
            else:
                if(check(loca[i][1], loca[i][2], loca[j][1], loca[j][2], loca[k][1], loca[k][2])) :
                    answer = min(answer, sum)

print(answer)