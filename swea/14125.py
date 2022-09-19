# 암호출력
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
secret = ["001101", "010011", "111011", "110001", "100011", "110111", "001011", "111101", "011001", "101111"]
for test in range(1, T+1):
    bit16 = input()
    bit2 = ""
    for i in bit16:  # 이진수로 변경
        tmp = ""
        if not i.isdigit():
            i = ord(i) - 55
        else:
            i = int(i)
        for j in range(4):
            tmp = str(i % 2) + tmp
            i = i // 2
        bit2 += tmp

    i = 0
    ans = []
    while i < len(bit2): # 암호 찾기
        if bit2[i:i+6] in secret:
            ans.append(secret.index(bit2[i:i+6]))
            i += 6
        else:
            i += 1
    print(f'#{test}', *ans)
