# 암호코드 스캔
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
code = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        tmp = input().rstrip()
        for i in tmp:
            if i != "0":
                lst.append(tmp)
    lst = list(set(lst))

    real = []  # 암호 부분만 찾아내기
    for k in range(len(lst)):
        lst2 = lst[k]
        i = 0
        while i < len(lst2):
            tmp = ""
            while i < len(lst2) and lst2[i] == "0":
                i += 1
            while i < len(lst2) and lst2[i] != "0":
                tmp += lst2[i]
                i += 1
            real.append(tmp)
    real = list(set(real))
    print(real)
    bit2 = []
    for k in real:
        if k == "":
            continue
        bit2tmp = "000"
        for i in k:  # 이진수로 변경
            tmp = ""
            if not i.isdigit():
                i = ord(i) - 55
            else:
                i = int(i)
            for j in range(4):
                tmp = str(i % 2) + tmp
                i = i // 2
            bit2tmp += tmp
        bit2.append(bit2tmp)
    print(bit2)
    ratio = [] # 비율 찾기
    for k in bit2:
        ratio.append(len(k)//56)
    print(ratio)

    bit2real = []
    for k in range(len(ratio)):
        # 암호 부분만 찾아내기
        if ratio[k] == 0:
            continue
        for i in range(len(bit2[k])):
            for j in range(8):
                if not (bit2[k][i + 7 * j:i + 7 * j + 7*ratio[k]:ratio[k]] in code):
                    break
            else:
                bit2real.append(bit2[k][i:i + 56 * ratio[k]:ratio[k]])
    print(bit2real)
    resnum = []
    for k in range(len(bit2real)):
        num = []  # 숫자로 변환하기
        for i in range(0, 56, 7):
            num.append(code.index(bit2real[k][i:i + 7]))
        resnum.append(num)
    print(resnum)
    ans = 0
    for k in resnum:
        state = 0  # 암호 맞는지 판별
        for i in range(0, len(k), 2):
            state += k[i] * 3 + k[i + 1]

        if state % 10 == 0:
            ans += sum(k)
    print(f'#{test} {ans}')

    # 해결xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx