T = int(input())

list_31 = [1,3,5,7,8,10,12]
for i in range(T) :
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:]

    str = f'#{i+1} {year}/{month}/{day}'
    if int(day) >=32 or int(day) <= 0 or int(month)<=0 or int(month)>12:
        print(f'#{i+1} -1')
    elif int(month) == 2 and int(day) > 28:
        print(f'#{i+1} -1')
    elif not int(month) in list_31 and int(day)>30 :
        print(f'#{i+1} -1')
    else :
        print(str)