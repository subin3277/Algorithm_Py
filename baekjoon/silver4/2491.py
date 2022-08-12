# 수열
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = list(map(int,input().split()))
maxcount = 0
count = 1
# 연속해서 커지는 경우
for i in range(N-1):
    if num_list[i] <= num_list[i+1]:
        count += 1
    else: # 작아지면
        maxcount = max(maxcount, count) # max 값 계산
        count = 1 # count 초기화
maxcount = max(maxcount, count)

# 연속해서 작아지는 경우
count = 1
for i in range(N-1):
    if num_list[i] >= num_list[i+1]:
        count += 1
    else: # 커지면
        maxcount = max(maxcount, count) # max 값 계산
        count = 1 # count 초기화
maxcount = max(maxcount, count)
print(maxcount)