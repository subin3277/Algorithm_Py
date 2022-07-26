T = int(input())
for i in range(T) :
    H, W, N = map(int,input().split())
    res = ''
    room = N//H +1
    floor = N%H
    if floor == 0 :
        floor = H
        room -= 1
    
    if room < 10 :
        res = '0'+str(room)
    else : 
        res = str(room)    
    res = str(floor) + res
    print(res)