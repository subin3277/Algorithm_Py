# 글자수
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str1 = input()
    str2 = input()
    str_dict = {}
    for i in str1:
        str_dict[i] = 0

    for i in str2:
        if str_dict.get(i, None) is not None: # key값이 존재하면
            str_dict[i] += 1 # 1 증가
    res = 0
    for i in str_dict.values(): # 딕셔너리 value 중 최대값 구하기
        if res < i:
            res = i
    print(f'#{test} {res}')