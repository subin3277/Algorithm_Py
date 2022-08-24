# 암호 생성기
import sys
sys.stdin = open("input.txt", "r")

T = 10
for test in range(1, T+1):
    N = int(input())
    queue = list(map(int, input().split()))
    res = True
    while True:
        for i in range(1, 6):
            t = queue.pop(0) - i # 큐의 맨앞 값 꺼낸 후 i 빼주기
            if t <= 0 : # 뺀 값이 0보다 작거나 같으면
                queue.append(0) # 0 추가하고
                res = False
                break # 중단
            queue.append(t)
        if not res:
            break
    print(f'#{test}', *queue)