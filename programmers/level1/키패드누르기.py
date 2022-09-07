# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    lloca = 10
    rloca = 12
    for i in numbers:
        if i == 1 or i == 4 or i== 7:
            answer += 'L'
            lloca = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            rloca = i
        else:
            if i == 0:
                i = 11
            if lloca == 1 or lloca == 4 or lloca == 7 or lloca == 10:
                ldis = abs(lloca + 1 - i)//3 + 1
            else:
                ldis = abs(lloca - i)//3
            if rloca == 3 or rloca == 6 or rloca == 9 or rloca == 12:
                rdis = abs(rloca - 1 - i)//3 + 1
            else:
                rdis = abs(rloca - i)//3

            if ldis == rdis:
                if hand == "left":
                    answer += "L"
                    lloca = i
                else:
                    answer += "R"
                    rloca = i
            elif ldis < rdis:
                answer += "L"
                lloca = i
            else:
                answer += "R"
                rloca = i
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))