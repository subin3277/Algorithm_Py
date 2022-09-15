# 홈 방범 서비스
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    home = []
    for i in range(N):
        home.append(list(map(int, input().split())))
    ans = 0
    for k in range(N+1, 0, -1):
        officemoney = k*k + (k-1)*(k-1) # 운영 비용
        for i in range(N):
            for j in range(N):
                count = 0
                for h in range(i - k + 1, i + k):
                    if not 0 <= h < N: # 리스트 바깥 값이면
                        continue # 계산 안함
                    start = j - (k-1) + abs(i - h) # 카운트 할 스타트
                    end = j + (k-1) - abs(i - h) # 카운트 할 엔트
                    if start < 0: # 범위 처리
                        start = 0
                    elif start >= N:
                        start = N-1
                    if end >= N:
                        end = N - 1
                    elif end < 0:
                        end = 0
                    count += home[h][start:end+1].count(1) # 집의 갯수 카운트
                res = count * M - officemoney # 이익 계산
                if res >= 0: # 손해보지 않았다면
                    ans = max(count, ans) # 최대 집 값
    print(f'#{test} {ans}')