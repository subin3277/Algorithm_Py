# 잃어버린 괄호

S = input()
lst = S.split('-')
stack = []
for i in lst:
    tmp = i.split('+')
    tmp_sum = 0
    for j in tmp:
        tmp_sum += int(j)
    stack.append(tmp_sum)
ans = stack.pop(0)
while stack:
    ans -= stack.pop(0)
print(ans)
