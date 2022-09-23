# 행렬과 연산

def shift(rc):
    tmp = rc.pop()
    rc.append(tmp)
    return rc

def rotate(rc):
    N = len(rc)
    M = len(rc[0])
    pre = rc[0][0]
    for j in range(M):
        nxt = rc[0][j]
        rc[0][j] = pre
        pre = nxt
    for i in range(1, N):
        nxt = rc[i][M-1]
        rc[i][M-1] = pre
        pre = nxt
    for i in range(M - 2, -1, -1):
        nxt = rc[N-1][i]
        rc[N-1][i] = pre
        pre = nxt
    for i in range(N - 2, -1, -1):
        nxt = rc[i][0]
        rc[i][0] = pre
        pre = nxt
    return rc

def solution(rc, operations):
    answer = rc
    for i in operations:
        if i == "Rotate":
            answer = rotate(rc)
        else:
            answer = shift(rc)
    return answer

rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]
print(solution(rc, operations))

# 해결xxxxxxxxxxxxxxxxxx