# 베이비진 게임
import sys
sys.stdin = open("input.txt", "r")

def sol(p):
    c = [0] * 12 # 카운트 배열

    for i in p:
        c[i] += 1 # 배열에 있는 값 하나씩 추가

    i = 0
    while i < 10:
        if c[i] >= 3: # 한개의 숫자가 3개이상이면 이김
            return True
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1: # 연속으로 3개있어도 이김
            return True
        i += 1
    return False

T = int(input())
for test in range(1, T+1):
    p = list(map(int, input().split()))
    p1 = [p[i] for i in range(0, 12, 2)]
    p2 = [p[i] for i in range(1, 12, 2)]

    res = 0
    for i in range(2, 6):
        if sol(p1[0:i+1]):
            res = 1
            break
        if sol(p2[0:i+1]):
            res = 2
            break
    print(f'#{test} {res}')
