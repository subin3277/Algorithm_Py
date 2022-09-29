# AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
ans = []
for test in range(T):
    p = input().rstrip() # 명령어
    N = int(input().rstrip()) # 배열에 들어있는 수
    tmp = input().rstrip()
    tmp = tmp[1:-1]
    num_list = deque()
    if tmp == '':
        ans.append('error')
        break
    else:
        num_list = deque(list(map(int, tmp.split(','))))

    reverse = False
    for i in p:
        if i == 'D':
            if not num_list:
                ans.append('error')
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
        ans.append(res)
for i in ans:
    print(i)

# 해결xxxxxxxxxxxxxxxxx