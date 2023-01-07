# 1 빼기

N = input()
lst = [(0, N)]
while lst:
    cnt, num = lst.pop(0)
    if num == 1:
        print(cnt)
        break
    lst.append((cnt+1,str(int(num)-1)))
    if "1" in num:
        if num.index("1") == 0:
            lst.append((cnt+1, str(num[1:])))
        elif num.index("1") == len(num)-1 :
            lst.append((cnt+1, str(num[:-1])))
        else:
            A, B = num[num.index("1")+1:],num[:num.index("1")]
            lst.append((cnt+1, str(int(A)+int(B))))