# 전화번호 목록

def solution(phone_book):   
    answer = True
    
    set_list = set()
    for i in phone_book:
        set_list.add(i)
    
    for i in phone_book:
        
        for j in range(len(i)):
            if i[0:j] in set_list:
                answer = False
                break
        if not answer:
            break
            
    return answer