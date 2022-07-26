a, b = map(int,input().split())

gcd = 1
min = min(a,b)
for i in range(min,0,-1) :
    if a%i == 0 and b%i == 0 :
        gcd = i
        break
lcm = a*b//gcd
print(gcd)
print(lcm)