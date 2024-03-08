def solution(gems):
    answer = [1, len(gems)]
    answer_len = len(gems)
    gem_kind = set(gems)
    gem_dict = {}
    
    start = 0
    end = 0
    while start <= end and start < len(gems) :   
        if len(gem_dict) == len(gem_kind) :
            if answer_len > end - start:
                answer_len = end - start
                answer = [start+1, end]

            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else :
                gem_dict[gems[start]] -= 1
            start += 1
            continue
            
        if end-start >= answer_len or end >= len(gems):
            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else :
                gem_dict[gems[start]] -= 1
            start += 1
            continue
        
        gem = gems[end]  
        gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
        end += 1
        
    return answer