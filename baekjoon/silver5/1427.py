# 소트인사이드

lst = list(map(int,input()))
ans = sorted(lst,reverse=True)
for i in range(len(ans)):
    print(ans[i], end='')
