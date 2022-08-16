# 백만장자 프로젝트
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    money = 0
    i = N-2
    max_idx = N - 1
    while i >= 0:
        if num_list[max_idx] > num_list[i]: # 기준 값이 앞 값보다 크면
            money -= num_list[i] # 앞의 값만큼 빼주고
            money += num_list[max_idx] # 기준 값만큼 더한다
            i -= 1
        else: # 아니면 기준값 갱신
            max_idx = i
            i = max_idx - 1

    if money < 0: # 이득이 음수일 때 0으로 출력
        money = 0

    print(f'#{test} {money}')
