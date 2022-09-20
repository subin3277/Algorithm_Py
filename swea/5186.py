# 이진수2
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = float(input())
    ans = ""
    ori = N
    count = 0
    while True:
        if N == 0:
            break
        N *= 2
        if N >= 1:
            ans += "1"
            N -= 1
        else:
            ans += "0"
        count += 1
        if count >= 13:
            ans = "overflow"
            break
    print(f'#{test} {ans}')