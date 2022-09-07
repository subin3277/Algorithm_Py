# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    singo = [[] for _ in range(len(id_list))]
    for i in report:
        A, B = map(str, i.split())
        singo[id_list.index(B)].append(A)
    for i in range(len(singo)):
        if len(singo[i]) >= k:
            for j in range(len(singo[i])):
                answer[id_list.index(singo[i][j])] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k)) # [2,1,1,0]