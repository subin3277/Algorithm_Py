# 연산자 끼워넣기
from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
A, B, C, D = map(int, input().split())
cal = ["+"] * A + ["-"] * B + ["*"] * C + ["/"] * D

maxres = -1000000000
minres = 1000000000
res = []
for p in tuple(set(permutations(cal))): # 모든 연산자 순열
    tmp = num_list[0]
    for k in range(1, len(num_list)): # 구한 연산자 순서대로 계산
        if p[k - 1] == '+':
            tmp += num_list[k]
        elif p[k - 1] == '-':
            tmp -= num_list[k]
        elif p[k - 1] == '*':
            tmp *= num_list[k]
        elif p[k - 1] == '/':
            if tmp < 0: # 음수 / 양수를 위한 처리
                tmp = (-tmp) // num_list[k] * (-1)
            else:
                tmp = tmp // num_list[k]
    res.append(tmp)

print(max(res)) # 최댓값
print(min(res)) # 최솟값