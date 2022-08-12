# 자기 방으로 돌아가기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    room_list = [0] * 200
    for i in range(N):
        room1, room2 = map(int, input().split())
        if room1 > room2: # 반대로 갈 경우 밑에 for문에 문제가 있으므로 교환
            room1, room2 = room2, room1
        for j in range((room1-1)//2, (room2-1)//2 + 1): # 지나가는 복도 색칠하기
            room_list[j] += 1
    res = max(room_list) # 가장 많이 지나야 하는 곳 확인
    print(f'#{test} {res}')