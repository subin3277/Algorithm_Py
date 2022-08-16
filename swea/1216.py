# 회문2
import sys
sys.stdin = open("input.txt", "r")

def judge(str1): # 회문 판단하는 함수
    for i in range(len(str1)//2):
        if str1[i] != str1[len(str1)-i-1]:
            return False
    return True

T = 10
for test in range(1, T+1):
    test_num = int(input())
    str_list = []
    for i in range(100):
        str_list.append(input())
    findlen = 100

    maxres = 0
    state = False

    while True:
        for i in range(100):
            # 세로 확인을 위한 문자열 생성
            htmp = ''
            for k in range(0, findlen):
                htmp += str_list[k][i]
            wtmp = str_list[i][0:findlen]
            for j in range(100-findlen+1):
                if judge(wtmp) or judge(htmp): # 가로 혹은 세로가 회문
                    maxres = findlen
                    state = True
                    break
                else:
                    if j + findlen < 100:
                        htmp = htmp[1::] + str_list[j + findlen][i]
                        wtmp = wtmp[1::] + str_list[i][j + findlen]
            if state:
                break
        if state:
            print(f'#{test} {maxres}')
            break
        else:
            findlen -= 1 # 최대 회문 길이 1 감소