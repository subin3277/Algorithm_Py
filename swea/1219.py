# 길찾기
import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    stack = []
    while True:
        for w in num_list[v]:
            if w == 99: # 도착점에 도착하는 것이면
                return 1 # 1 리턴
            if not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0

T = 10
for test in range(1, T+1):
    Tnum, N = map(int, input().split())
    num_list = [[] for _ in range(100)]
    input_list = list(map(int, input().split()))
    for i in range(0, N*2, 2):
        num_list[input_list[i]].append(input_list[i+1])
    visited = [False]*100
    res = dfs(0)
    print(f'#{test} {res}')