# 직사각형
import sys
sys.stdin = open("input.txt", "r")

T = 4
for test in range(1, T+1):
    point_list = list(map(int, input().split()))
    rec1 = point_list[0:4]
    rec2 = point_list[4:8]

    # 서로 만날 수 없는 상황
    if rec1[0] > rec2[2] or rec1[2] < rec2[0] or rec1[1] > rec2[3] or rec1[3] < rec2[1]:
        res = 'd'
    # 한점에서 만나는 상황
    elif (rec1[1] == rec2[3] or rec1[3] == rec2[1]) and (rec1[2] == rec2[0] or rec1[0] == rec2[2]):
        res = 'c'
    # 한 선분이 만나는 상황
    elif rec1[2] == rec2[0] or rec1[0] == rec2[2] or rec1[1] == rec2[3] or rec1[3] == rec2[1]:
        res = 'b'
    else: # 그외는 모두 직사각형
        res = 'a'

    print(res)
