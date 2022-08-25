# 피자굽기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    for i in range(M):
        pizza[i] = (i+1, pizza[i]) # 피자번호 함께 저장
    queue = pizza[0:N] # 초기 화덕에 넣을 것
    i = N
    while len(queue) != 1: # 피자가 1개만 남을 때 까지
        t = queue.pop(0) # 1번 위치 피자 꺼내기
        if t[1] != 0: # 치즈가 0이 아니면
            queue.append((t[0], t[1]//2)) # 치즈 반으로 감소
        else:
            if i < M: # 치즈가 0이어서 뺐으면
                queue.append((pizza[i][0], pizza[i][1]//2)) # 새로 넣기
                i += 1

    print(f'#{test} {queue[0][0]}')