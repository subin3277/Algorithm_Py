# 피보나치 함수

T = int(input())
lst = []
for test in range(1, T+1):
    lst.append(int(input()))
res = [[1, 0], [0, 1], [1, 1]]
for i in range(3, max(lst) + 1):
    res.append([res[-1][0] + res[-2][0], res[-1][1] + res[-2][1]])
for i in lst:
    print(res[i][0], res[i][1])