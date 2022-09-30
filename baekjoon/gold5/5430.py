# AC
from collections import deque

T = int(input())
for test in range(T):
    p = input() # 명령어
    N = int(input()) # 배열에 들어있는 수
    tmp = input()[1:-1].split(",")
    num_list = deque(tmp)

    if N == 0:
        num_list = []

    reverse = False
    for i in p:
        if i == 'D':
            if not num_list:
                print('error')
                break
            else:
                if reverse:
                    num_list.pop()
                else:
                    num_list.popleft()

        elif i == 'R':
            reverse = not reverse
    else:
        if reverse:
            num_list.reverse()
        res = "[" + ",".join(num_list)+"]"
        print(res)

# 해결xxxxxxxxxxxxxxxxx