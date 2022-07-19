a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (b if a>b else a) if ((b if a>b else a)<c) else c
print(int(d))