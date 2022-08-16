# 의석이의 세로로 말해요
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str_list = []
    res = ''
    max_len = 0
    for i in range(5):
        str = input()
        str_list.append(str)
        if len(str) > max_len: # 입력문자열 중 가장 긴 길이 찾기
            max_len = len(str)
    for i in range(max_len):
        for j in range(5):
            if i < len(str_list[j]): # i 값이 해당 문자열의 길이보다 짧을 때만 출력값에 저장
                res += str_list[j][i]

    print(f'#{test} {res}')