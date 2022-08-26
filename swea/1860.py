# 진기의 최고급 붕어빵
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M, K = map(int, input().split())
    second = list(map(int, input().split()))

    for i in range(N-1): # 손님 방문순서 정렬
        for j in range(i+1, N):
            if second[i] > second[j]:
                second[i], second[j] = second[j], second[i]

    now_sec = 0
    fishbread = [0] * (second[-1] + 1)
    for i in range(1, second[-1]+1):
        if i % M == 0: # 해당 초마다 되면 붕어빵 개수 증가
            fishbread[i] = fishbread[i-1] + K
        else:
            fishbread[i] = fishbread[i-1]

    res = True
    for i in second:
        if fishbread[i] == 0: # 붕어빵이없으면
            res = False # Impossible
            break
        else:
            for j in range(i, len(fishbread)): # 있으면 이후 붕어빵 1개씩 감소
                fishbread[j] -= 1
    if res:
        print(f'#{test} Possible')
    else:
        print(f'#{test} Impossible')