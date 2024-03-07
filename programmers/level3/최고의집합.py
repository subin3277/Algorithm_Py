def solution(n, s):
    if s < n : return [-1]
    answer, mod = [s//n] * n, s % n
    for i in range(mod) : answer[len(answer) -1 - i] += 1
    return answer