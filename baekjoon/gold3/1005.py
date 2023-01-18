# ACM Craft

T = int(input()) # 테스트 케이스
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    order = [[] for i in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        order[Y].append(X)
    print(order)
    W = int(input())

    stack = order[W]
    stack2 = []
    ans = 0
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
        stack = stack2
        stack2 = []