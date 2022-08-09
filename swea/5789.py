import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for text in range(1, T+1):
    N, Q = map(int, input().split())
    # 박스 리스트 생성
    box_list = [0]*N
    for i in range(Q):
        L, R = map(int, input().split())
        # L부터 R까지(인덱스틑 0부터 이므로 L-1)
        for j in range(L-1, R):
            # box_list 값 변경 (인덱스로 인해 i+1)
            box_list[j] = i+1
    print(f'#{text}', *box_list)