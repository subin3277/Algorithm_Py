# 창고 다각형
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
floor_list= []
maxV = 0
maxid = 0
for i in range(N):
    L, H = map(int, input().split())
    floor_list.append([L, H])
    if H > maxV:
        maxV = H
        maxid = L

# 버블 정렬 이용하여 정렬
for j in range(N-1, 0, -1):
    for k in range(0, j):
        if floor_list[k][0] > floor_list[k+1][0]:
            floor_list[k], floor_list[k+1] = floor_list[k+1], floor_list[k]

res = 0
# 오른쪽으로 가기
for i in range(N-1):
    # 가장 큰 값이 있는 곳까지 가면 스탑
    if floor_list[i][0] == maxid:
        break
    # 다음 있는 값이 더 크면 그 전까지 있던 값 균일하게 만들기
    if floor_list[i][1] > floor_list[i+1][1]:
        floor_list[i+1][1] = floor_list[i][1]
    # 층수들 더하기
    res += (floor_list[i+1][0]-floor_list[i][0])*floor_list[i][1]

# 왼쪽으로 오기
for i in range(N-1,-1,-1):
    if floor_list[i][0] == maxid:
        break
    # 이전에 있는 값이 더 작으면 큰값으로 만들기
    if floor_list[i][1] > floor_list[i-1][1]:
        floor_list[i-1][1] = floor_list[i][1]
    res += (floor_list[i][0]-floor_list[i-1][0])*floor_list[i][1]
res += maxV
print(res)
