# 컨테이너 운반
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split())) # 화물무게
    t = list(map(int, input().split())) # 트럭 적재용량

    w.sort(reverse=True) # 내림차순 정렬
    t.sort(reverse=True)
    res = 0
    while w and t: # 둘중 하나라도 없어질 때 까지
        wt = w.pop(0)
        tt = t.pop(0)
        if wt <= tt: # 트럭 적재용량이 더 크거나 같으면
            res += wt # 결과에 추가
        else: # 아니면
            t.insert(0, tt) # 트럭 적재용량에 다시 추가

    print(f'#{test} {res}')