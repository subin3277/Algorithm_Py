# 국회의원 선거
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
vote = [0] * N
for i in range(N):
    vote[i] = int(input())

res = 0
if N != 1:
    while True:
        maxidx = maxres = -1
        for i in range(N): # 최대 득표자 찾기
            if maxres <= vote[i]:
                maxres = vote[i]
                maxidx = i
        if maxidx != 0: # 1번이 아니면
            vote[maxidx] -= 1 # 한표가져오기
            vote[0] += 1
            res += 1
        else: # 맞으면 종료
            break

print(res)
