# Z

def solution(N, x1, y1):
    global cnt
    if x1 == r and y1 == c:
        print(cnt)
        exit(0)
    if N == 1:
        cnt += 1
        return
    if x1 <= r <= x1 + N//2 and y1 <= c <= y1 + N // 2:
        solution(N // 2, x1, y1)
    else:
        cnt += (N // 2) * (N // 2)
    if x1 <= r <= x1 + N//2 and y1 + N // 2 <= c <= y1 + N:
        solution(N // 2, x1, y1 + N // 2)
    else:
        cnt += (N // 2) * (N // 2)
    if x1 + N // 2 <= r <= x1 + N and y1 <= c <= y1 + N // 2:
        solution(N // 2, x1 + N // 2, y1)
    else:
        cnt += (N // 2) * (N // 2)
    if x1 + N // 2 <= r <= x1 + N and y1 + N // 2 <= c <= y1 + N:
        solution(N // 2, x1 + N // 2, y1 + N // 2)
    else:
        cnt += (N // 2) * (N // 2)



N, r, c= map(int, input().split())
cnt = 0
solution(2**N, 0, 0)