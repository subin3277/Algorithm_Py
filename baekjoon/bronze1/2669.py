# 직사각형 네개의 합집합의 면적 구하기
import sys
sys.stdin = open("input.txt", "r")

rect = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            rect[i][j] = 1 # 입력된 사각형 위치에 1로 표시

count = 0
for i in range(100):
    for j in range(100):
        if rect[i][j] == 1:
            count += 1 # 1로 표시된 곳의 개수
print(count)