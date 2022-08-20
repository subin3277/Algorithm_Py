# 쉬운 거스름돈
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    prize = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = [0] * 8
    for i in range(8):
        count[i] += N // prize[i] # 줘야 할 화폐장수 계산
        N = N % prize[i] # 남은 돈
    print(f'#{test}')
    print(*count)