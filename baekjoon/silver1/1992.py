# 쿼드 트리

def solution(x, y, n):
    global ans
    target = lst[x][y]
    tmp = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if target == lst[i][j]:
                tmp += 1

    if tmp == n * n:
        ans += str(lst[x][y])
    else:
        ans += "("
        solution(x, y, n//2)
        solution(x, y + n // 2, n // 2)
        solution(x + n//2, y, n//2)
        solution(x + n//2, y + n//2, n//2)
        ans += ")"


N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input())))

ans = ""
solution(0, 0, N)
print(ans)