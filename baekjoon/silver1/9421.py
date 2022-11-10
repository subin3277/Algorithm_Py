# 소수 상근수

N = int(input())
lst = [False] * (N+1)
for i in range(2, N+1):
    if lst[i]:
        continue
    j = i
    while j+i < N+1:
        j += i
        lst[j] = True

ans = []
for i in range(2, N+1):
    if lst[i]:
        continue
    sumlst = []
    tmp = 0
    num = i
    while tmp != 1:
        tmp = 0
        while num > 0:
            tmp += (num%10)**2
            num = num//10
        if tmp in sumlst:
            break
        sumlst.append(tmp)
        num = tmp
    else:
        ans.append(i)
for i in ans:
    print(i)