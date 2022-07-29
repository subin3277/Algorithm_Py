X = int(input())

i= 0
sum = 0
while sum < X :
    sum += i
    i+=1


top = i-1 - (sum-X)
bottom = 1 + (sum-X)
if (i-1) % 2 != 0 :
    top, bottom = bottom, top
print(f'{top}/{bottom}')