def dfs(node, graph, visited, component):
    """
    Depth-first search to find connected components
    """
    stack = [node]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            component.add(current + 1)  # Convert to 1-based indexing
            # Add all unvisited neighbors
            for neighbor in range(len(graph)):
                if graph[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

def find_components(graph):
    n = len(graph)
    
    # Create undirected version for weak components
    undirected = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or graph[j][i] == 1:
                undirected[i][j] = 1
    
    # Find strongly connected components (using directed graph)
    strong_visited = set()
    strong_components = []
    
    for node in range(n):
        if node not in strong_visited:
            component = set()
            dfs(node, graph, strong_visited, component)
            if component:
                strong_components.append(component)
    
    # Find weakly connected components (using undirected graph)
    weak_visited = set()
    weak_components = []
    
    for node in range(n):
        if node not in weak_visited:
            component = set()
            dfs(node, undirected, weak_visited, component)
            if component:
                weak_components.append(component)
    
    return (f"Strongly Connected Components (Strong): {strong_components}\n"
            f"Weakly Connected Components (Weak): {weak_components}")

# Test with the given graph
if __name__ == '__main__':
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 0, 1, 0, 0, 0],  # 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  # 6
        [0, 0, 1, 0, 1, 1, 0, 1, 0],  # 7
        [0, 0, 1, 0, 0, 0, 0, 0, 1],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
    ]
    result = find_components(G)
    print(result)