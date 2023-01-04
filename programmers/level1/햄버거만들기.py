# 햄버거 만들기

def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        if i == 1 and len(stack) >= 3: # 빵이 올려지고 4개 이상 쌓였을때
            if stack[-3:] == [1,2,3]:
                for _ in range(3):
                    stack.pop()
                answer += 1
                continue
        stack.append(i)
    return answer

ingredient = [2,1,1,2,3,1,2,3,1]
#ingredient = [1,3,2,1,2,1,3,1,2]
print(solution(ingredient))