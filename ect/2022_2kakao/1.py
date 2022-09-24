def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    term_dic = dict()
    for i in terms:
        A, B = map(str, i.split())
        term_dic[A] = int(B)
    for i in range(len(privacies)):
        date, kind = map(str, privacies[i].split())
        p_y, p_m, p_d = map(int, date.split("."))
        p_y += term_dic[kind] // 12
        p_m += term_dic[kind] % 12
        p_d -= 1
        if p_d == 0:
            p_d = 28
            p_m -= 1
            if p_m == 0:
                p_y -= 1
                p_m = 12
        if p_m > 12:
            p_m -= 12
            p_y += 1

        if t_y > p_y:
            answer.append(i + 1)
        elif t_y == p_y:
            if t_m > p_m:
                answer.append(i + 1)
            elif t_m == p_m:
                if t_d > p_d:
                    answer.append(i + 1)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", " 2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))