# 최소 직사각형
def solution(sizes):
    answer = 0
    width = []
    height = []
    for i,j in sizes:
        width.append(max(i,j))
        height.append(min(i,j))
    answer = max(width)*max(height)
    return answer