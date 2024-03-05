from itertools import combinations

def solution(relation):
    answer = 0
    answer_list = []
    col = [i for i in range(len(relation[0]))]
    for i in range(len(col) + 1) :
        for j in combinations(col,i) :
            tmp_set = []
            for k in range(len(relation)) :
                tmp_set2 = []
                for l in j:
                    tmp_set2.append(relation[k][l])
                if tmp_set2 not in tmp_set :
                    tmp_set.append(tmp_set2)

            if len(tmp_set) == len(relation):
                for x in answer_list :
                    if len(x - set(j)) > 0 :
                        continue
                    else:
                        break
                else:
                    answer_list.append(set(j))
                    answer += 1
                        
    return answer