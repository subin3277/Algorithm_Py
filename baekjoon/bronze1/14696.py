# 딱지놀이
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
for i in range(N):
    A, *a_list = map(int, input().split())
    B, *b_list = map(int, input().split())
    for j in range(4, 0, -1): # 별, 원, 사각형, 삼각형 순서로
        a_count = a_list.count(j) # 개수 세기
        b_count = b_list.count(j)
        if a_count != b_count: # 개수가 다르면
            if a_count > b_count: # 이긴 사람 찾기
                res = 'A'
            else:
                res = 'B'
            break
    else:
        res = 'D'
    print(res)