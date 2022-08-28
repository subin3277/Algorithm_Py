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
            if count>= 10: # 한줄에 10개 작성했으면
                print() # 줄 바꾸기
                list = '' # 리스트 초기화
                count=0 # 카운트 초기화
            count+=1
            print(str,end='')
    print()
