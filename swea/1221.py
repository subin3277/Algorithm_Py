# GNS
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test in range(1, T+1):
    Test, N = map(str, input().split())
    str_list = list(map(str, input().split()))

    N = int(N)

    for i in range(N):
        str_list[i] = number.index(str_list[i])

    for i in range(N - 1):  # 선택정렬로 정렬
        minIndex = i
        for j in range(i + 1, N):
            if str_list[minIndex] > str_list[j]:  # 해당 문자열에 맞는 인덱스(=integer 값)
                minIndex = j
        str_list[i], str_list[minIndex] = str_list[minIndex], str_list[i]

    for i in range(N):
        str_list[i] = number[str_list[i]]

    print(f'{Test}')
    print(*str_list)