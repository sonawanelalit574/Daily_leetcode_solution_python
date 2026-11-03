from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Count the number of complete connected components in an undirected graph.
        A complete component is one where every pair of vertices is connected by an edge.
      
        Args:
            n: Number of vertices in the graph (0 to n-1)
            edges: List of edges where each edge is [u, v]
      
        Returns:
            Number of complete connected components
        """
      
        def dfs(node: int) -> tuple[int, int]:
            """
            Perform DFS to explore a connected component.
          
            Args:
                node: Current node to explore
          
            Returns:
                Tuple of (vertex_count, edge_count) in this component
            """
            # Mark current node as visited
            visited[node] = True
          
            # Initialize counts: 1 vertex (current), degree of current node
            vertex_count = 1
            edge_count = len(adjacency_list[node])
          
            # Explore all neighbors
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    # Recursively explore unvisited neighbors
                    vertices, edges = dfs(neighbor)
                    vertex_count += vertices
                    edge_count += edges
          
            return vertex_count, edge_count
      
        # Build adjacency list representation of the graph
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
      
        # Initialize visited array to track explored vertices
        visited = [False] * n
      
        # Count complete components
        complete_component_count = 0
      
        # Process each connected component
        for vertex in range(n):
            if not visited[vertex]:
                # Get vertex and edge counts for this component
                vertices, edges = dfs(vertex)
              
                # Check if component is complete
                # In a complete graph with v vertices: edges = v * (v - 1)
                # Since each edge is counted twice in adjacency list
                if vertices * (vertices - 1) == edges:
                    complete_component_count += 1
      
        return complete_component_count
