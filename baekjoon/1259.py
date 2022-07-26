while True :
    num = input()
    if num == '0' :
        break
    
    length = len(num)
    if length % 2 == 0 :
        for i in range(length//2) :
            if num[i] != num[length-i-1] :
                print('no')
                break
        else : print('yes')
    else :
        for i in range(length//2) :
            if num[i] != num[length-i-1] :
                print('no')
                break
        else : print('yes')