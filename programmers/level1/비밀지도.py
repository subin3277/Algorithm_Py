# 비밀지도

def solution(n, arr1, arr2):
    tmp1 = []
    tmp2 = []
    answer = []
    for N in arr1:
        i = N
        res = ''
        for _ in range(n):
            res = str(i%2) + res
            i //= 2
        tmp1.append(res)
    for N in arr2:
        i = N
        res = ''
        for _ in range(n):
            res = str(i%2) + res
            i //= 2
        tmp2.append(res)

    for i in range(n):
        res = ''
        for j in range(n):
            if tmp1[i][j] == '0' and tmp2[i][j] == '0':
                res += ' '
            else:
                res += '#'
        answer.append(res)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n ,arr1, arr2))