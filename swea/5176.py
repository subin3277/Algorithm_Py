# 이진탐색
import sys
sys.stdin = open("input.txt", "r")

def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)
        num_list[n] = cnt
        cnt += 1
        inorder(n*2+1)

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = [0]*(N+1)
    cnt = 1
    inorder(1)

    print(f'#{test} {num_list[1]} {num_list[N//2]}')
