# 이진수
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, bit16 = map(str, input().split())
    bit2 = ""
    for i in bit16:  # 이진수로 변경
        tmp = ""
        if not i.isdigit():
            i = ord(i) - 55
        else:
            i = int(i)
        for j in range(4):
            tmp = str(i % 2) + tmp
            i = i // 2
        bit2 += tmp
    print(f'#{test} {bit2}')