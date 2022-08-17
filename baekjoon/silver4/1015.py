# 수열 정렬
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
sort_list = num_list.copy()
rank_list = [0]*N
for i in range(N-1): # 버블 정렬
    for j in range(i+1, N):
        if sort_list[i] > sort_list[j]:
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

for i in range(N):
    rank_list[num_list.index(sort_list[i])] = i # 순서대로 값 넣기
    num_list[num_list.index(sort_list[i])] = 0 # 이후 인덱스 찾기에 방해 안되도록 0으로 설정
print(*rank_list)