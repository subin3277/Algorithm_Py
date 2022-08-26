# 욕심쟁이 돼지
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    bap = list(map(int, input().split()))
    nextbap = [0] * 6
    count = 1
    while True:
        if sum(bap) > N: # 필요한 사료가 하루 제공량 보다 더 많으면
            break # 중단
        else:
            count += 1

        for i in range(6): # 다음날 사료 계산하기
            if i == 0:
                nextbap[i] = bap[i] + bap[-1] + bap[i] + bap[i+1]
            elif i == 5:
                nextbap[i] = bap[i] + bap[i - 1] + bap[i] + bap[0]
            else:
                nextbap[i] = bap[i] + bap[i-1] + bap[i] + bap[i+1]
        bap = nextbap.copy()
    print(count)