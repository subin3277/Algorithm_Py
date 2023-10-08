def solution(triangle):
    answer = 0

    for i in range(len(triangle)-2, -1, -1) :
        for j in range(len(triangle[i])) :
            tmp = max(triangle[i+1][j], triangle[i+1][j+1])
            triangle[i][j] += tmp

    answer = triangle[0][0]
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))