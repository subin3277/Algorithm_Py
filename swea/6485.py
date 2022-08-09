import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N = int(input())
    bus_list = [0] * N
    # 버스가 지나는 모든 정류장 리스트
    for i in range(N):
        A, B = map(int, input().split())
        tmp = []
        for j in range(A, B+1):
            tmp.append(j)
        bus_list[i] = tmp

    P = int(input())
    res_list = [0] * P
    # 입력받은 C 정류장 지나는지 판단
    for i in range(P):
        C = int(input())
        # 모든 버스에 대해서
        for j in bus_list:
            # 지나는 정류장 리스트에 C가 있다면
            if C in j:
                # 횟수 1 추가
                res_list[i] += 1
    print(f'#{test}', *res_list)