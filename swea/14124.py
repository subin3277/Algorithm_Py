# 십육진수의 십진수 출력
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    bit16 = input()
    bit2 = ""
    for i in bit16: # 이진수로 변경
        tmp = ""
        if not i.isdigit():
            i = ord(i)-55
        else:
            i = int(i)
        for j in range(4):
            tmp = str(i%2) + tmp
            i = i // 2
        bit2 += tmp
    res = []
    for i in range(len(bit2)//7): # 7개씩 끊어서 10진수로 변경
        ans = tmp = 0
        for j in range(i*7+6, i*7-1, -1):
            if bit2[j] == "1":
                ans += 2**tmp
            tmp += 1
        res.append(ans)
    ans = tmp = 0
    for i in range(len(bit2) - 1, len(bit2) - len(bit2)%7 - 1, -1): # 남은거 10진수로 변경
        if bit2[i] == "1":
            ans += 2 ** tmp
        tmp += 1
    res.append(ans)
    print(f'#{test}', *res)