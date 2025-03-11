import heapq

# Create the adjacency matrix for the given graph G
# Nodes are labeled as A, B, C, D, E, F, G, H, L, M
class Graph:
    def __init__(self, nodes, edges):
        self.node_map = {node: idx for idx, node in enumerate(nodes)}
        self.adj_list = [[] for _ in nodes]
        
        for start, end, weight in edges:
            self.add_edge(start, end, weight)
    
    def add_edge(self, a, b, weight):
        i = self.node_map[a]
        j = self.node_map[b]
        self.adj_list[i].append((j, weight))
        self.adj_list[j].append((i, weight))
    
    def dijkstra(self, source, target):
        if source not in self.node_map or target not in self.node_map:
            return None, float('inf')
        
        start = self.node_map[source]
        end = self.node_map[target]
        n = len(self.adj_list)
        
        distances = [float('inf')] * n
        prev = [None] * n
        distances[start] = 0
        heap = [(0, start)]
        
        while heap:
            dist, current = heapq.heappop(heap)
            if current == end:
                break
            if dist > distances[current]:
                continue
                
            for neighbor, weight in self.adj_list[current]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev[neighbor] = current
                    heapq.heappush(heap, (new_dist, neighbor))
        
        return self._reconstruct_path(prev, end, distances[end])
    
    def _reconstruct_path(self, prev, end, distance):
        if distance == float('inf'):
            return [], -1
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = prev[current]
        
        idx_to_node = {v: k for k, v in self.node_map.items()}
        return [idx_to_node[idx] for idx in reversed(path)], distance

# Khởi tạo đồ thị
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
edges = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]

graph = Graph(nodes, edges)

# Xử lý input/output
def get_valid_node(prompt):
    while True:
        node = input(prompt).strip().upper()
        if node in graph.node_map:
            return node
        print(f"Invalid node. Valid nodes are: {', '.join(nodes)}")

source = get_valid_node("Enter source node (A-M): ")
target = get_valid_node("Enter target node (A-M): ")

path, total_weight = graph.dijkstra(source, target)

if path:
    print(f"Shortest path: {' -> '.join(path)}")
    print(f"Total weight: {total_weight}")
else:
    print("No path exists between the specified nodes.")