# ACM Craft

T = int(input()) # 테스트 케이스
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    order = [[] for i in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        order[Y].append(X)

    W = int(input())

    stack = order[W]
    stack2 = []
    ans = time[W]
    while True:
        tmp = 0
        while stack:
            t = stack.pop()
            tmp = max(tmp, time[t])
            stack2 += order[t]
        ans += tmp
        if not stack2:
            print(ans)
            break
        stack = list(set(stack2))
        stack2 = []

# 해결 xxxxxxxxxx