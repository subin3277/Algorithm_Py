# 숫자 게임
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    i = j = 0
    while i < len(A) and j < len(B) :
        if A[i] < B[j] :
            answer += 1
            i += 1
            j += 1
        elif A[i] > B[i] :
            i += 1
        else:
            i += 1
    return answer