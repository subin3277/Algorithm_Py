#의상

def solution(clothes):
    answer = 1
    dict = {}
    for i, j in clothes:
        if dict.get(j, -1) == -1:
            dict[j] = [i]
        else:
            dict.get(j).append(i)
    for v in dict.values():
        answer *= len(v)+1
    return answer - 1