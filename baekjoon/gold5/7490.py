# 0 만들기
T = int(input())

def BT(sum, idx, res, flag) :
    if idx == N:
        if sum == 0:
            print(res)
        return
    
    if flag == "+" :
        nsum = sum + idx * 10 + 1
    elif flag == '-' :
        nsum = sum - idx * 10 - 1
    
    if flag != " ":
        BT(nsum, idx+1, res+" "+str(idx+1), " ")
    BT(sum+(idx+1), idx+1, res+"+"+str(idx+1), "+")
    BT(sum-(idx+1), idx+1, res+"-"+str(idx+1), "-")

for _ in range(T) :
    N = int(input())

    BT(1, 1, "1", "+")
    print()