# 수 이어가기
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
max_sol = []
max_count = 0
for i in range(N, 0, -1):
    sol = [N, i]
    while True:
        num = sol[-2] - sol[-1] # 맨 뒤에서 두번째, 첫번째 값 빼주기
        if num < 0: # 음수가 됐다면
            if max_count < len(sol): # 최대 길이라면 값들 갱신
                max_count = len(sol)
                max_sol = sol.copy()
            break # 멈추기
        else:
            sol.append(num)
print(max_count)
print(*max_sol)