N = int(input())

for i in range(N) :
    ox = str(input())
    score = 0
    con_count = 1
    for j in ox : 
        if j == 'O' :
            score += con_count
            con_count += 1
        else :
            con_count = 1
    print(score)