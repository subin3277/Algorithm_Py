# 나무 조각
import sys
sys.stdin = open("input.txt", "r")

num_list = list(map(int, input().split()))
while True:
    for i in range(4):
        if num_list[i] > num_list[i+1]: # 더 크면 교환
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            print(*num_list) # 출력하기
    if num_list == [1, 2, 3, 4, 5]: # [1, 2, 3, 4, 5]와 같으면 멈추기
        break