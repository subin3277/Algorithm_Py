T = int(input())

# k층 n호
def resident(k,n) :
    if n == 1 :
        return 1
    elif k == 0 :
        return n
    else :
        return resident(k,n-1)+resident(k-1,n)

for i in range(T) :
    k = int(input())
    n = int(input())
    print(resident(k,n))
