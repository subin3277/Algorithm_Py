# 부분집합의 합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1,T+1):
    N, K = map(int,input().split())
    #  집합 A 생성
    num_list = [0]*12
    for i in range(12):
        num_list[i] = i+1

    #  값 만족하는 count 변수
    count = 0
    #  2*12번의 반복문
    for i in range(1<<12):
        tmp_list = []
        tmp_sum = 0
        for j in range(12):
            if i & (1 << j):
                tmp_list.append(num_list[j])
                tmp_sum += num_list[j]
        # 부분집합의 원소개수가 N개 and 원소의 합이 K
        if len(tmp_list) == N and tmp_sum == K :
            count += 1
    print(f'#{test} {count}')