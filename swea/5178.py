# 노드의 합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M, L = map(int, input().split())
    ans = [0] * (N+1)

    for i in range(M):
        n, x = map(int, input().split())
        ans[n] = x

    start = len(ans) - M - 1 # 노드값 넣기 시작할 곳
    x = 1
    while N >= x:
        x *= 2
    for i in range(x-N-1):
        ans.append(0) # 모든 자식 노드가 2개씩이도록 리스트 추가

    length = N
    if N % 2 == 0:
        length += 1

    for i in range(length, 0, -2):
        if start == 0 or start == L-1: # 원하는 인덱스 도달시
            break
        ans[start] = ans[i] + ans[i-1] # 밑의 노드합
        start -= 1

    print(f'#{test} {ans[L]}')