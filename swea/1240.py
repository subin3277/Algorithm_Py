# 단순 2진 암호코드
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    code = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    for _ in range(N):
        tmp = input()
        if "1" in tmp: # 암호 있는 행만 추가
            lst.append(tmp)
    lst2 = lst[0]
    real = "" # 암호 부분만 찾아내기
    for i in range(len(lst2)):
        for j in range(8):
            if not(lst2[i+7*j:i+7*j+7] in code):
                break
        else:
            real = lst2[i:i+56]
    num = [] # 숫자로 변환하기
    for i in range(0, 56, 7):
        num.append(code.index(real[i:i+7]))
    state = 0 # 암호 맞는지 판별
    for i in range(0, len(num), 2):
        state += num[i] * 3 + num[i+1]
    ans = 0
    if state % 10 == 0:
        ans = sum(num)
    print(f'#{test} {ans}')


