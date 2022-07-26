x, y, w, h = map(int,input().split())

res = min(x,y)
if w-x < res :
    res = w-x
if h-y < res :
    res = h-y
print(res)