# 색종이
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
num_list = []
for _ in range(101):
    num_list.append([0]*101) # 빈 도화지 생성
count = 0
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(10): # 색종이 종이 10*10 동안
        for j in range(10):
            if num_list[x+i][y+j] == 0: # 붙힌적 없다면
                count += 1 # 넓이 1 증가
                num_list[x+i][y+j] += 1 # 붙혔다고 값 1증가
print(count)