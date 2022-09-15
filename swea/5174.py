# subtree
import sys
sys.stdin=open("input.txt","r")

T = int(input())
for test in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    par = [0] * (E+2) # 인덱스:노드 / 리스트 값:부모
    ch1 = [0] * (E+2) # 인덱스:부모 / 리스트 값:왼쪽노드
    ch2 = [0] * (E+2)

    for i in range(0, 2*E, 2):
        P = lst[i]
        C = lst[i+1]
        if ch1[P] == 0:
            ch1[P] = C
        else:
            ch2[P] = C
        par[C] = P
    count = 1
    n = N
    stack = [n]
    while stack:
        t = stack.pop(0)
        if ch1[t] != 0:
            stack.append(ch1[t])
            count += 1
        if ch2[t] != 0:
            stack.append(ch2[t])
            count += 1
    print(f'#{test} {count}')