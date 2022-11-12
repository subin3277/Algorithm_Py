def solution(edges, roots):
    answer = [0]*len(edges)

    pre_edge = edges.copy()
    for new_root in roots:
        new_edge = []
        for k in range(len(edges)):
            i, j = edges[k]
            if j == new_root:
                i,j = j,i
                for h in range(len(new_edge)):
                    x,y = new_edge[h]
                    if y==j:
                        new_edge[h] = [y,x]
            new_edge.append([i, j])
        for k in range(len(edges)):
            if pre_edge[k] != new_edge[k]:
                answer[k] += 1
        pre_edge = new_edge.copy()

    return answer

edg = [[1,3],[1,2],[2,4],[2,5]]
roots = [2,3]
edg2 = [[1,2],[1,3],[2,4]]
roots2 = [3,4,1,2]
print(solution(edg, roots))