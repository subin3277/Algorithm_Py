# 이진탐색
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1,T+1):
    N, D= map(int,input().split())
    num_list = list(map(int,input().split()))
    lp = 0
    rp = N
    center = int((lp+rp)/2)
    num = num_list[center]
    res = -1
    while num != D:
        if lp == rp or lp+1 == rp: # 같거나 없으면
            res = -1
            break
        if num > D: # D보다 크면 오른쪽 기준점 center로
            rp = center
        elif num < D: # D보다 작으면 왼쪽 기준점 center로
            lp = center
        center = int((lp + rp) / 2) # 가운데 인덱스 갱신
        num = num_list[center] # 가운데 값 갱신
        res = center # 인덱스 저장
    print(f'#{test} {res+1}')