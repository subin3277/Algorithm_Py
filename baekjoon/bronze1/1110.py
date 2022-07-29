N = int(input())

new = -1
num = str(N)
count = 0

while N!=new :
    if int(num) < 10 :
        num = '0'+num
    plus = (int(num[0])+int(num[1]))%10
    new = (int(num[1])) * 10 + plus
    num = str(new)
    count += 1
print(count)