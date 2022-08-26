# 줄세우기
import sys
sys.stdin = open("input.txt", "r")

P = int(input())
for _ in range(P):
    N, *tall = list(map(int, input().split()))

    count = 0
    for i in range(19, 0, -1):
        for j in range(i):
            if tall[j+1] < tall[j]:
                tall[j+1], tall[j] = tall[j], tall[j+1]
                count += 1
    print(N, count)