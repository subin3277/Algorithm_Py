def solution(players, callings):
    answer = players
    score = {}
    for i in range(len(players)):
        score[players[i]] = i
    print(score)
    for i in callings:
        score[i] -= 1
    return answer


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))
