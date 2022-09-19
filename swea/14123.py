# 이진수의 십진수 출력
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    inputbit = input()
    res = []
    for i in range(len(inputbit)//7):
        ans = 0
        tmp = 0
        for j in range(i*7+6, i*7-1, -1):
            if inputbit[j] == "1":
                ans += 2**tmp
            tmp += 1
        res.append(ans)
    print(f'#{test}', *res)