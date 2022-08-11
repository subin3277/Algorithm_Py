# 이진탐색
import sys
sys.stdin = open("input.txt", "r")

# 이진 탐색 함수
def findbook(P, N):
    count = 0
    lp = 1 # 왼쪽 기준점
    rp = P # 오른쪽 기준점
    while True:
        cp = int((lp + rp) / 2) # 중간 값 찾기
        if cp > N: # N이 중간값보다 왼쪽에 있으면
            rp = cp # 오른쪽 기준점을 중간값으로 변경
        elif cp < N: # N이 중간값보다 오른쪽에 있으면
            lp =cp # 왼쪽 기준점을 중간값으로 변경
        else:
            break # 같으면 반복문 종료
        count += 1
    return count # 탐색 횟수 리턴

T = int(input())
for test in range(1, T+1):
    P, A, B = map(int, input().split())
    count_A = findbook(P, A)
    count_B = findbook(P, B)
    if count_A < count_B: # A가 더 적은 횟수면 A 승리
        res = 'A'
    elif count_A > count_B: # B가 더 적은 횟수면 B 승리
        res = 'B'
    else: # 같으면 비김
        res = '0'
    print(f'#{test} {res}')