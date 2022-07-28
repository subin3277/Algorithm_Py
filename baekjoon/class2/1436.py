N = int(input())

count = 0
num = 666
while True :
    if count == N :
        print(num-1)
        break
    elif '666' in str(num) or '6666' in str(num):
        count += 1
    num+=1
