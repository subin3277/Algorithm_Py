# 원재의 메모리 복구하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    bit = list(map(int, input()))
    res = [0] * len(bit) # 바꾼 값 저장할 리스트
    count = 0

    for i in range(len(bit)): # 길이 동안
        if res == bit: # 같아지면 중단
            break
        if bit[i] != res[i]: # 다르면
            count += 1 # 횟수 증가 후에
            for j in range(i, len(bit)): # 끝까지 반대로 변경
                res[j] = 1-res[j]
    print(f'#{test} {count}')