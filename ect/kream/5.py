def minimumTreePath(n, edges, visitNodes):
    # Create adjacency list representation of the tree
    adjacency_list = {}
    for u, v in edges:
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Set to store visited nodes
    visited = set()

    def dfs(node):
        stack = [(node, set())]  # (node, visited_nodes_set)
        while stack:
            current_node, visited_nodes = stack.pop()
            if current_node in visitNodes and current_node not in visited_nodes:
                visited_nodes.add(current_node)
                if visited_nodes == set(visitNodes):
                    return True
            visited.add(current_node)
            for adjacent_node in adjacency_list[current_node]:
                if adjacent_node not in visited:
                    stack.append((adjacent_node, visited_nodes.copy()))

        return False

    # Start DFS from node 1
    return dfs(1)

n= 3
edges = [(1,2), (1,3)]
visitNodes = [2]
print(minimumTreePath(n, edges, visitNodes))