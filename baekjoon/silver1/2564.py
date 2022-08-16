# 경비원
import sys
sys.stdin = open("input.txt", "r")

W, H = map(int, input().split())
N = int(input())
mar_list = []
for i in range(N):
    tmp = list(map(int, input().split()))
    mar_list.append(tmp)
loca = list(map(int, input().split())) # 동근이 위치
mar_list.append(loca)
maxres = 0
res = 0
for i in range(N+1):
    if mar_list[i][0] == 2: # 남
        mar_list[i][1] += H
    elif mar_list[i][0] == 4: # 동
        mar_list[i][1] += W

for i in range(N):
    if mar_list[i][0] + mar_list[N][0] == 5 or mar_list[i][0] == mar_list[N][0] : # 같거나 마주볼 때
        maxres = abs(mar_list[i][1] - mar_list[N][1])
    elif mar_list[i][0] + mar_list[N][0] == 6: # 2, 4번에 있을 때
        maxres = (W+H)*2 - (mar_list[i][1] + mar_list[N][1])
    else:
        maxres = mar_list[i][1] + mar_list[N][1]

    if maxres >= W+H:
        maxres = (W + H)*2 - maxres
    res += maxres
    print(maxres)
print(res)

