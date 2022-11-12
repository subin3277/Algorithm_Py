
def solution(reference, track):
    ans = []

    def dfs(G, v, l, m_l):
        for i in range(len(l), 0, -1):
            tmp = G[v:i + v]
            if i + v -1 < len(G) and G[v:i + v] in l:
                dfs(G, i + v, l, m_l + [i] )
        if sum(m_l) == len(G):
            ans.append(min(m_l))

    dfs(track, 0, reference, [])
    answer = max(ans)
    return answer

reference = "abc"
track= "bcab"
reference2 = "vxrvip"
track2 = "xrviprvipvxrv"
print(solution(reference, track))