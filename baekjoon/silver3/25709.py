# 1 빼기

N = input()
lst = [(0, N)]
while lst:
    cnt, num = lst.pop(0)
    if int(num) == 0:
        print(cnt)
        break
    lst.append((cnt+1, str(int(num)-1)))
    if "1" in num:
        tmp = list(filter(lambda x:num[x] == "1", range(len(num))))
        for i in tmp:
            if i == 0:
                if num[1:]!="":
                    lst.append((cnt+1, num[1:]))
                else:
                    lst.append((cnt+1, "0"))
            elif i == len(num)-1:
                if num[:-1]!="":
                    lst.append((cnt+1, num[:-1]))
                else:
                    lst.append((cnt+1, "0"))
            else:
                A, B = num[i+1:], num[:i]
                lst.append((cnt+1, str(int(A)+int(B))))
# 해결 xxxxxxxxxxxxxxxxxxxx