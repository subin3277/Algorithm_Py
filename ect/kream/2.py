def findRange(num):
    strnum = str(num)
    for i in strnum:
        if i != '9':
            max_res = strnum.replace(i, '9')
            break
    else:
        max_res = strnum

    if strnum[0] != '1' :
        min_res = strnum.replace(strnum[0], '1')
    else :
        for i in strnum:
            if i != '1' and i != '0':
                change_min = i
                min_res = strnum.replace(change_min, '0')
                break
        else:
            min_res = strnum

    print(max_res)
    print(min_res)
    return int(max_res) - int(min_res)

num = 909
print(findRange((num)))