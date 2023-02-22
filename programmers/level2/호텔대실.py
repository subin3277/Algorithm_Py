# 호텔대실

def solution(book_time):
    answer = 0

    timelist = [[0]*60 for _ in range(24)]

    for i in book_time:
        starthour, startmin = map(int, i[0].split(':'))
        endhour, endmin = map(int, i[1].split(':'))

        for j in range(starthour, endhour+1):
            for k in range(60):
                if j == starthour and k < startmin:
                    continue
                elif j == endhour and k >= endmin:
                    break
                else:
                    timelist[j][k] += 1

        for j in range(10):
            if endmin + j >= 60:
                timelist[endhour+1][(endmin+j)%60] += 1
            else :
                timelist[endhour][endmin+j] += 1
    for tmp in timelist:
        answer = max(answer, max(tmp))

    return answer

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
# book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))