from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    discount = [0.9, 0.8, 0.7, 0.6]
    ratio = []
    prize = []
    for i in users:
        ratio.append((100 - i[0])/100)
        prize.append(i[1])
    for p in product(discount, repeat=len(emoticons)):
        plus = 0
        t_sum = [0] * len(users)
        for i in range(len(users)):
            for j in range(len(emoticons)):
                if ratio[i] >= p[j]:
                    t_sum[i] += emoticons[j] * p[j]
            if t_sum[i] >= prize[i]:
                plus += 1
                t_sum[i] = 0
        money = int(sum(t_sum))
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = money
        elif answer[0] == plus:
            answer[1] = max(answer[1], money)
    return answer

user = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(user, emoticons))