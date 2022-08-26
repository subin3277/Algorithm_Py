# 낚시터 자리잡기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    G = []
    P = []

    for i in range(3):
        Gate, Person = map(int, input().split())
        G.append(Gate)
        P.append(Person)
    minans = 1200

    pcount = 0
    fish = [-1] + [0] * N
    for k in range(1):
        j = 0
        pcount = 0
        while pcount < P[k]:
            if fish[G[k] - j] == 0:
                fish[G[k] - j] = abs(j) + 1
                pcount += 1
            elif fish[G[k] - j] == -1:
                break
            j += 1
        j = 1
        while pcount < P[k]:
            if G[k] + j <= N and fish[G[k] + j] == 0:
                fish[G[k] + j] = abs(j) + 1
                pcount += 1
            j += 1

    for k in range(1, 3):
        pcount = 0
        j = 0
        while pcount < P[k]:
            if G[k] - j >= 0 and fish[G[k] - j] == 0:
                fish[G[k] - j] = abs(j) + 1
                pcount += 1

            if G[k] + j <= N and fish[G[k] + j] == 0:
                fish[G[k] + j] = abs(j) + 1
                pcount += 1

            j += 1
    if minans > sum(fish[1::]):
        minans = sum(fish[1::])

    G[0], G[2] = G[2], G[0]
    P[0], P[2] = P[2], P[0]

    pcount = 0
    fish = [-1] + [0] * N
    for k in range(1):
        j = 0
        pcount = 0
        while pcount < P[k]:
            if G[k] + j <= N and fish[G[k] + j] == 0:
                fish[G[k] + j] = abs(j) + 1
                pcount += 1
            elif G[k] + j > N:
                break
            j += 1
        j = 1
        while pcount < P[k]:
            if G[k] - j > 0 and fish[G[k] - j] == 0:
                fish[G[k] - j] = abs(j) + 1
                pcount += 1
            j += 1

    for k in range(1, 3):
        pcount = 0
        j = 0
        while pcount < P[k]:
            if G[k] - j >= 0 and fish[G[k] - j] == 0:
                fish[G[k] - j] = abs(j) + 1
                pcount += 1
            if G[k] + j <= N and fish[G[k] + j] == 0:
                fish[G[k] + j] = abs(j) + 1
                pcount += 1
            j += 1
        #     elif G[k] + j > N:
        #         break
        #     j += 1
        # j = 1
        # while pcount < P[k]:
        #     if G[k] - j >= 1 and fish[G[k] - j] == 0:
        #         fish[G[k] - j] = abs(j) + 1
        #         pcount += 1
        #     j += 1
    if minans > sum(fish[1::]):
        minans = sum(fish[1::])

    print(f'#{test} {minans}')