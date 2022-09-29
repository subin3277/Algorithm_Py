# 원자 소멸 시뮬레이션
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    arr = []
    x = y = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        tmp[2], tmp[3] = tmp[3], tmp[2]
        arr.append(tmp)
        x.append(tmp[0])
        y.append(tmp[1])

    tbl = [0, 1, 2, 3]
    dx = [0, 0, -1, 1] # 상하좌우
    dy = [1, -1, 0, 0]
    ans = 0

    while len(arr) > 0:
        i = 0
        while i < len(arr):
            arr[i][0] = arr[i][0] + dx[arr[i][3]]
            arr[i][1] = arr[i][1] + dy[arr[i][3]]
            if not (min(x) <= arr[i][0] <= max(x) and min(y) <= arr[i][1] <= max(y)):
                arr.pop(i)
            else:
                i += 1
        arr.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)

        i = 1
        while i < len(arr):
            if arr[i-1][0:2] == arr[i][0:2]:
                ans += (arr[i-1][2] + arr[i][2])
                arr.pop(i)
                arr.pop(i-1)
            else:
                i += 1
    print(f'#{test} {ans}')

    # 해결xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx