# 수열
import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

sum = 0
for i in range(K):
    sum += tem_list[i] # 초기 K개의 합
max_tem = sum
for i in range(1, N-K+1):
    sum -= tem_list[i-1] # 지난 값 빼기
    sum += tem_list[i+K-1] # 다음 값 더하기
    if sum > max_tem: # 최대값인지 비교하기
        max_tem = sum
print(max_tem)