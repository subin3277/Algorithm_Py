# 전위순회
import sys
sys.stdin = open("input.txt", "r")

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i

def preorder(n):
    if n:
        print(n, end=" ")
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    V = N
    par = [0]*(V+1) # 자식을 인덱스로 부모 번호저장
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(N-1):
        p, c = num_list[i*2], num_list[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p
    root = num_list[0]
    print(f'#{test}', end= " ")
    preorder(root)