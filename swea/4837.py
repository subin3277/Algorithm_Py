#부분 집합 합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    num_list = list(map(int, input().split()))

    state = False
    # 공집합 제외하기 위해 1 ~ 1<<10
    for i in range(1, 1 << 10):
        # 부분집합 원소의 합
        res = 0
        for j in range(10):
            if i & (1 << j):
                res += num_list[j]
        # 합이 0이라면 반복문 break, state는 True
        if res == 0:
            state = True
            break
    # state가 True 라면
    if state:
        print(f'#{test} 1')
    # False 라면
    else:
        print(f'#{test} 0')