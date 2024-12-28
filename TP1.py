class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def path_exists(self, start, end, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
            
        path.append(start)
        visited.add(start)
        
        if start == end:
            return True, path
            
        if start not in self.graph:
            path.pop()
            return False, []
            
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                exists, current_path = self.path_exists(neighbor, end, visited, path)
                if exists:
                    return True, current_path
                    
        path.pop()
        return False, []

def main():
    # Create and initialize the graph
    g = Graph()
    # Add edges
    edges = [
        (1, 2),
        (2, 5),
        (3, 6),
        (4, 6),
        (4, 7),
        (6, 7)
    ]
    
    for u, v in edges:
        g.add_edge(u, v)
        
    try:
        start = int(input("Enter start node: "))
        end = int(input("Enter end node: "))
        exists, path = g.path_exists(start, end)
        
        if exists:
            path_str = " -> ".join(str(node) for node in path)
            print(f"Path exists between node {start} and node {end} (path: {path_str})")
        else:
            print(f"No path exists between node {start} and node {end}")
            
    except ValueError:
        print("Please enter valid integer node numbers")

if __name__ == "__main__":
    main()