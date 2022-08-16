# 줄세우기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
num_list = list(map(int, input().split()))
res_list = [] # 결과 저장 리스트
for i in range(1, T+1):
    res_list.insert(len(res_list)-num_list[i-1], i) # i를 이미 줄 선 길이 - 뽑은 수의 위치에 삽입
print(*res_list)