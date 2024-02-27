# 색종이
import sys

N = int(input())
rect_list = [[0]*1001 for _ in range(1001)]
for k in range(1, N+1):
    x, y, w, h = map(int, sys.stdin.readline().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            rect_list[i][j] = k # 입력된 곳의 위치에 순서번호 입력


for j in range(1, N+1):
    count = 0
    for i in rect_list:
        count += i.count(j) # 입력된 갯수 구하기
    print(count)