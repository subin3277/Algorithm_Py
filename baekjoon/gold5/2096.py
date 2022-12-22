# 내려가기

N = int(input())
max_list = [0]*3
min_list = [0]*3

max_tmp = [0]*3
min_tmp = [0]*3

for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_list[j], max_list[j+1])
            min_tmp[j] = a + min(min_list[j], min_list[j+1])
        elif j == 1:
            max_tmp[j] = b + max(max_list[j], max_list[j + 1], max_list[j-1])
            min_tmp[j] = b + min(min_list[j], min_list[j + 1], min_list[j-1])
        else:
            max_tmp[j] = c + max(max_list[j], max_list[j - 1])
            min_tmp[j] = c + min(min_list[j], min_list[j - 1])

    for j in range(3):
        max_list[j] = max_tmp[j]
        min_list[j] = min_tmp[j]
print(max(max_list), min(min_list))