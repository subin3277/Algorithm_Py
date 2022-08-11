# 일곱 난쟁이
import sys
sys.stdin = open("input.txt", "r")

T = 9
tall_list = [0]*T
for i in range(T):
    tall_list[i] = int(input())
tall_list.sort() # 정렬

nanjang1 = nanjang2 = 0
state = True
for i in range(T-1):
    for j in range(i,T):
        res = sum(tall_list)
        res -= (tall_list[i] + tall_list[j]) # 선택한 두개의 값을 뺀다
        if res == 100: # 뺀 값이 100이 된다면 그 두명이 눈쟁이가 아님
            nanjang1 = tall_list[i]
            nanjang2 = tall_list[j]
            state = False # 이중루프 나가기 위해
            break
    if not state:
        break

# 위에서 찾은 2명이 아니면 프린트
for i in tall_list:
    if i != nanjang1 and i != nanjang2:
        print(i)