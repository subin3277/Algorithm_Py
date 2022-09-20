# 1로 만들기
X = int(input())
lst = [0, 0, 1, 1]

for i in range(4, X + 1):
    lst.append(lst[i-1] + 1)
    if i % 2 == 0:
        lst[i] = min(lst[i], lst[i//2] + 1)
    if i % 3 == 0:
        lst[i] = min(lst[i], lst[i//3] + 1)
print(lst[X])