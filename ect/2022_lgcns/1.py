from itertools import combinations
def solution(marbles):
    answer = []
    marbles.sort()
    sumlst = (0,)
    if len(marbles)% 2:
        for i in range(len(marbles)):
            tmp = marbles.copy()
            tmp[i] = 0
            for j in range(1,len(tmp)):
                for c in combinations(tmp,j):
                    if sum(c)*2 == sum(tmp):
                        if sum(sumlst) < sum(c):
                            sumlst = c + (marbles[i],)
    else:
        for j in range(1, len(marbles)):
            for c in combinations(marbles, j):
                if sum(c) * 2 == sum(marbles):
                    if sum(sumlst) < sum(c):
                        sumlst = c
    sumlst = list(sumlst)

    for i in sumlst:
        marbles.remove(i)
    center = []
    if len(sumlst) != len(marbles):
        center = [sumlst[-1]]
        sumlst = sumlst[:len(sumlst)-1]
    sumlst.sort()
    marbles.sort()
    if sumlst[0] > marbles[0]:
        answer = marbles + center + sumlst
    else :
        answer = sumlst + center + marbles

    return answer

marbles1 = [1,2,3,4,4]
marbles2 = [5,5,1,4]
marbles3 = [3,9,7,5]
print(solution(marbles3))