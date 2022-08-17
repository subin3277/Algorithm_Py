# 종이자르기
import sys
sys.stdin = open("input.txt", "r")

W, H = map(int, input().split())
N = int(input())
W_list = [0, W] # 첫값, 끝값 삽입
H_list = [0, H] # 첫값, 끝값 삽입
for i in range(N):
    A, B = map(int, input().split())
    if A == 0:
        H_list.append(B)
    else:
        W_list.append(B)
W_list.sort() # 정렬
H_list.sort() # 정렬
W_max = 0
H_max = 0
for i in range(len(W_list)-1): # 가로의 최대 차 구하기
    tmp = W_list[i+1] - W_list[i]
    if tmp > W_max:
        W_max = tmp
for i in range(len(H_list)-1): # 세로의 최대 차 구하기
    tmp = H_list[i + 1] - H_list[i]
    if tmp > H_max:
        H_max = tmp
print(W_max * H_max)