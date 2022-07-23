T = int(input())

for i in range (T):
    N = int(input())
    count = 0
    print('#%d'%(i+1))
    list=''
    for j in range (N):
        str, num = input().split()
        num = int(num)
        for k in range (num):
            if count>= 10:
                print()
                list = ''
                count=0
            count+=1
            print(str,end='')
    print()
