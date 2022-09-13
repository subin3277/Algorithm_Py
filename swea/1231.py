# 중위순회
import sys
sys.stdin = open("input.txt", "r")

def order(n):
    if n:
        order(ch1[n])
        print(word[n], end="")
        order(ch2[n])

T = 10
for test in range(1, T+1):
    N = int(input())
    num_list = []
    word = [0]*(N+1)
    for i in range(N):
        tmp = list(map(str, input().split()))
        word[int(tmp[0])] = tmp[1]
        if len(tmp) >= 3:
            for j in range(len(tmp)-2):
                num_list.append(int(tmp[0]))
                num_list.append(int(tmp[j+2]))
    V = N
    par = [0] * (V + 1)  # 자식을 인덱스로 부모 번호저장
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(N - 1):
        p, c = num_list[i * 2], num_list[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p
    root = num_list[0]
    print(f'#{test}', end=" ")
    order(root)
    print()