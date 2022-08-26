# 두개의 숫자열
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    difflen = 0 # 두 리스트 길이의 차
    if N > M: # 길이 같게 만들어주기(앞에 0넣으면서)
        B = [0] * (N - M) + B
        difflen = N - M
    else:
        A = [0] * (M - N) + A
        difflen = M - N

    maxres = -1000000

    for j in range(difflen + 1): # 두 길이의 차이만큼 비교
        res = 0
        for i in range(len(A)): # 각 항목 곱한 후 더하기
            res += A[i] * B[i]
        if maxres < res: # 최댓값 비교하기
            maxres = res
        if N > M: # N이 더 크면 B를 옮기기
            t = B.pop(0)
            B.append(t)
        else:
            t = A.pop(0) # M이 더 크면 A를 옮기기
            A.append(t)
    print(f'#{test} {maxres}')