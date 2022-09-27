# 이진 탐색
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    ans = 0
    for i in B:
        l = 0
        r = N - 1
        swapstate = -1
        state = False
        while l <= r:
            mid = (l+r)//2
            if A[mid] == i:
                state = True
                break
            elif A[mid] > i:
                if swapstate == -1 or swapstate == 1:
                    state = True
                    swapstate = 0
                else:
                    state = False
                    break
                r = mid - 1
            else:
                if swapstate == -1 or swapstate == 0:
                    swapstate = 1
                    state = True
                else:
                    state = False
                    break
                l = mid + 1
        if state and i in A:
            ans += 1
    print(f'#{test} {ans}')