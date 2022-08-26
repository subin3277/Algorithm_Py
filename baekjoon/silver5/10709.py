# 기상캐스터
import sys
sys.stdin = open("input.txt", "r")

H, W = map(int, input().split())
cloud = []
sol = []
for _ in range(H):
    cloud.append(list(map(str, input())))
    sol.append([-1] * W)

for i in range(H):
    for j in range(W):
        if cloud[i][j] == 'c': # 구름이 있는 곳이면
            for k in range(j, W): # 그 자리부터 끝까지
                sol[i][k] = 0 # 0으로 갱신
        elif sol[i][j] != -1: # 구름이 지나갈 자리라면
            for k in range(j, W): # 그자리부터 끝까지
                sol[i][k] += 1 # 1씩 증가
for i in range(H):
    print(*sol[i])