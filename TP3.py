"""
TP3 Exercise
Given a graph G and a binary tree T, implement the following:
a) Create a function to construct an adjacency matrix for a directed graph G with:

Input: List of edges and number of nodes
Each edge is a tuple (u,v) representing a directed edge from u to v
Nodes are numbered from 1 to n
Example edges: [(1,2), (1,3), (2,5), (2,6), (3,4), (4,8), (5,7)]
       1
     /   \
    3     2
   /     / \
  4     6   5
 /           \
8             7

b) Implement a binary tree with the following requirements:

Create a TreeNode class with label, left child, and right child
Implement inorder traversal algorithm
Create a function to find a subtree with a given root value
Allow user to input a value and print inorder traversal of the subtree rooted at that value
"""

from typing import List, Tuple, Optional
from collections import defaultdict

class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u: int, v: int) -> bool:
        if not (1 <= u <= self.num_nodes and 1 <= v <= self.num_nodes):
            print(f"Invalid edge: ({u}, {v})")
            return False
        self.adj_matrix[u - 1][v - 1] = 1
        self.adj_list[u-1].append(v-1)
        return True
    
    def construct_from_edges(self, edges: List[Tuple[int, int]]) -> None:
        for u, v in edges:
            self.add_edge(u, v)
    
    def print_matrix(self) -> None:
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

class TreeNode:
    def __init__(self, label: int):
        self.label = label
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def construct_specific_tree(self) -> None:
        """Construct the specific tree structure as per the problem"""
        # Create the root
        self.root = TreeNode(1)
        
        # Level 1
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(2)
        
        # Level 2
        self.root.left.left = TreeNode(4)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(5)
        
        # Level 3
        self.root.left.left.left = TreeNode(8)
        self.root.right.right.left = TreeNode(7)
    
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder_helper(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder_helper(node.left)
            result.append(node.label)
            inorder_helper(node.right)
            
        inorder_helper(root)
        return result
    
    def find_subtree(self, x: int) -> Optional[TreeNode]:
        if not self.root:
            return None
            
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            if node.label == x:
                return node
            left_result = dfs(node.left)
            if left_result:
                return left_result
            return dfs(node.right)
            
        return dfs(self.root)

def main():
    # Graph construction
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
    graph = Graph(8)
    graph.construct_from_edges(edges)
    graph.print_matrix()
    
    # Binary tree construction and operations
    tree = BinaryTree()
    tree.construct_specific_tree()  # Construct the specific tree structure
    
    while True:
        try:
            x = int(input("\nEnter root value for subtree traversal (or -1 to exit): "))
            if x == -1:
                break
                
            subtree = tree.find_subtree(x)
            if subtree:
                result = tree.inorder(subtree)
                print(f"Inorder traversal of subtree rooted at {x}: {' '.join(map(str, result))}")
            else:
                print(f"No node found with value {x}")
        except ValueError:
            print("Please enter a valid integer")

if __name__ == "__main__":
    main()