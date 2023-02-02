# 분산처리

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    a = A % 10

    if a == 0 :
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4,9]:
        b = B % 2
        if b == 0:
            print(a*a%10)
        else:
            print(a)
    else:
        b = B%4
        if b == 0:
            print(a**4%10)
        else:
            print(a**b%10)