# 문자열 비교
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    str1 = input()
    str2 = input()
    state = False
    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]: # 슬라이싱해서 같다면
            state = True
            break
    if state:
        print(f'#{test} 1')
    else :
        print(f'#{test} 0')