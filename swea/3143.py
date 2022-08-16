# 가장 빠른 문자열 타이핑
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str1, str2 = map(str, input().split())
    count = 0
    i = 0
    str1_len = len(str1)
    str2_len = len(str2)
    while i < str1_len-str2_len+1:
        if str1[i:i+str2_len] == str2: # str2의 길이만큼 자르기
            count += 1
            i += str2_len-1
        i += 1
    res = len(str1) - (len(str2)-1)*count
    print(f'#{test} {res}')