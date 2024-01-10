# 숫자카드

N = int(input())
N_lst = set(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    if i in N_lst:
        print(1, end=" ")
    else:
        print(0, end=" ")
