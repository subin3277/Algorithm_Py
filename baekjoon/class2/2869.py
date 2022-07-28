A, B, V = map(int,input().split())

day = A-B
count = (V-B)//day
if (V-B)%day != 0 :
    count += 1
print(count)
