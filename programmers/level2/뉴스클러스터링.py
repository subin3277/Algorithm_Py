# 뉴스 클러스터링

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalnum() and str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalnum() and str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])

    if str1_list == [] and str2_list == []:
        return 65536

    inter = union = 0
    tmp = []
    tmp2 = []
    for i in str1_list:
        if i in str2_list and not (i in tmp):
            inter += min(str1_list.count(i), str2_list.count(i))
            tmp.append(i)
        if not i in tmp2:
            union += max(str1_list.count(i), str2_list.count(i))
            tmp2.append(i)
    for i in str2_list:
        if not i in tmp2:
            union += max(str1_list.count(i), str2_list.count(i))
            tmp2.append(i)
    answer = int((inter / union) * 65536)
    return answer

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2)) #43690