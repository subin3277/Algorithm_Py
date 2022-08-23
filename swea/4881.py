# 배열 최소 합
import sys
sys.stdin = open("input.txt", "r")

def backtrack(j): # 0 ~ N-1 까지의 모든 순열 찾기
    global sumres, tmp

    if tmp > sumres: # 실행중 최소값 보다 커지면
        return # 바로 중단
    if j == N: # stack의 갯수가 N일때
        if tmp < sumres:
            sumres = tmp
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            tmp += num_list[j][i]
            backtrack(j+1)
            tmp -= num_list[j][i]
            visited[i] = False

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = []
    for _ in range(N):
        num_list.append(list(map(int, input().split())))

    visited = [False] * N
    stack = []
    tmp = 0
    sumres = N * 10 # 최소 합
    backtrack(0)
    print(f'#{test} {sumres}')