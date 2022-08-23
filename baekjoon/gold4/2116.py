# 주사위 쌓기
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dice = []
for i in range(N):
    dice.append(list(map(int, input().split())))
maxsum = 0
for i in range(6):
    nxtidx = i
    sum = 0
    for j in range(N):
        num = [1, 2, 3, 4, 5, 6] # 하나씩 지울 리스트
        nxtnum = dice[j][nxtidx]
        num.remove(nxtnum) # 밑에 있는 수 지우기
        # 다음 숫자의 인덱스 찾기
        if nxtidx == 0 or nxtidx == 5:
            nxtnum = dice[j][5 - nxtidx]
        elif nxtidx == 1 or nxtidx == 2:
            nxtnum = dice[j][nxtidx + 2]
        else:
            nxtnum = dice[j][nxtidx - 2]
        num.remove(nxtnum) # 마주보고 있는 수 지우기
        sum += max(num) # 나머지 값들중 최댓값 더하기
        if j != N - 1:
            nxtidx = dice[j+1].index(nxtnum)
    if maxsum < sum:
        maxsum = sum
print(maxsum)