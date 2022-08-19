# 방 배정
import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
num_list = [[0]*6, [0]*6] # 남 / 여
for i in range(N):
    S, C = map(int, input().split())
    if S == 0: # 남/여 별 학년 별 갯수 세기
        num_list[1][C - 1] += 1
    else:
        num_list[0][C - 1] += 1

count = 0
for i in num_list:
    for j in i:
        count += j // K # 방 나눠주기
        if j % K != 0: # 남는 인원있다면
            count += 1 # 방 하나 추가
print(count)