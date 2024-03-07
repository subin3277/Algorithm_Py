from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words :
        return answer
    
    visit = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    
    def check(word1, word2) :
        cnt = 0
        word_list = list(word2)
        for i in list(word1):
            if cnt > 1 : return False
            if i in word_list :
                word_list.remove(i)
            else :
                cnt += 1
        if cnt == 1:
            return True
        
    while queue :
        t, cnt = queue.popleft()
        
        for i in range(len(words)) :
            if not visit[i] and check(t, words[i]) :
                visit[i] = True
                if words[i] == target:
                    return cnt+1
                else:
                    queue.append((words[i], cnt+1))
    
    return answer