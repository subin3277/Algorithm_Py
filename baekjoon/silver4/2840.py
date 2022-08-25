# 행운의 바퀴
import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
wheel = [0] * N
res = ''
bfidx = 0
for i in range(K):
    S, alpha = map(str, input().split())
    state = True
    for j in range(N): # 중복값 확인하기
        if wheel[j] == alpha and j != (bfidx+int(S)) % N:
            state = False
            break
    # 바퀴에 있는 값이 0이 거나 넣을 값과 같다면
    if state and wheel[(bfidx + int(S)) % N] == 0 or wheel[(bfidx + int(S)) % N] == alpha:
        wheel[(bfidx + int(S)) % N] = alpha # 값을 넣고
        bfidx += int(S) # 인덱스 더해주기
    else: # 아니면
        res = '!' # 존재하지않는다
        break
if res != '!':
    for i in range(N):
        if wheel[i] == alpha: # 마지막 글자의 위치 찾기
            strat = i
            break
    for i in range(N, 0, -1):
        if wheel[(strat+i) % N] == 0: # 0이면 ? 추가
            res += '?'
        else:
            res += wheel[(strat+i) % N]
print(res)