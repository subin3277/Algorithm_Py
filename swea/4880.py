# 토너먼트 카드게임
import sys
sys.stdin = open("input.txt", "r")

def card(ls, rs):
    sidx = ls
    ridx = rs

    if sidx == ridx: # 원소가 1개 일때
        stack.append(num_list[sidx])
        return stack, ls, rs
    if sidx + 1 == ridx: # 2개일 때
        if (num_list[sidx][1] - num_list[ridx][1] + 3) % 3 == 2: # 앞에 있는 숫자가 졌을 때
            stack.append(num_list[ridx])
        else: # 이기거나 비겼을 때
            stack.append(num_list[sidx])
        return stack, ls, rs
    card(ls, (ls + rs) // 2) # 반으로 나눠 앞부분
    card((ls + rs) // 2 + 1, rs) # 반으로 나눠 뒷부분
    return stack, ls, rs

T = int(input())
for test in range(1, T+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    num_list = []
    for i in range(N):
        num_list.append((i+1, tmp[i]))
    stack = []
    i = N-1
    while True:
        num_list = card(0, i)[0]
        stack = []
        if len(num_list) <= 1: # 결과값이 1개만 남을 때 까지
            res = num_list.pop()
            break
        else:
            i = len(num_list) - 1 # 결과값이 2개 이상일 때 한번더
    print(f'#{test} {res[0]}')