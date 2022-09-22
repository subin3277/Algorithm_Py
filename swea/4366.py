# 정식이의 은행업무
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    bit2 = input()
    bit3 = input()

    for i in range(len(bit2)):
        newbit2 = bit2[0:i] + str(1-int(bit2[i])) + bit2[i+1::] # 한자리씩 바꿔보기
        bit10 = 0
        tmp = len(bit2) - 1
        for j in range(len(newbit2)): # 이진수를 십진수로 바꾸기
            bit10 += int(newbit2[j]) * (2**tmp)
            tmp -= 1
        newbit3 = ""
        tmp = bit10
        for j in range(len(bit3)): # 십진수를 삼진수로 바꾸기
            newbit3 = str(tmp % 3) + newbit3
            tmp //= 3
        cnt = 0
        for j in range(len(bit3)): # 추측한 답이 맞는지 확인하기
            if bit3[j] != newbit3[j]:
                cnt += 1
                if cnt > 1:
                    break
        else:
            print(f'#{test} {bit10}')
            break