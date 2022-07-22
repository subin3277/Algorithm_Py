str = input()
str= str.upper()
al_list = []
count_list = []
for i in str :
    if i in al_list :
        count_list[al_list.index(i)] += 1
    else :
        al_list.append(i)
        count_list.append(1)
tmp = count_list.copy()
tmp.sort(reverse=True)


if len(tmp)>1 and tmp[0] == tmp[1] :
    print('?')
else:
    max = al_list[count_list.index(max(count_list))]
    print(max)