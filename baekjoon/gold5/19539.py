# 사과나무

N = int(input())
tree = list(map(int, input().split()))

if sum(tree) % 3 != 0 :
    print("NO")
else :
    cnt = 0
    for i in tree:
        cnt += i//2
    if cnt >= sum(tree)//3 :
        print("YES")
    else :
        print("NO")