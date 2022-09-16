# Contact
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    N, S = map(int, input().split())
    num = list(map(int, input().split()))
    lst = [[] for _ in range(101)]
    visited = [False] * 101 # 방문 리스트
    for i in range(0, N, 2): # 리스트 만들기
        lst[num[i]].append(num[i+1])

    stack = [S]
    visited[S] = True # 방문
    while True:
        if len(stack) == 0:
            break
        res = stack.copy() # 전단계에서 방문했던 숫자 저장
        for i in range(len(stack)):
            t = stack.pop(0)
            for j in lst[t]: # 연락 가능한 숫자에 대해
                if not visited[j]: # 방문하지 않았던 곳이라면
                    visited[j] = True # 방문표시
                    stack.append(j) # 다음 방문을 위한 저장

    print(f'#{test} {max(res)}')