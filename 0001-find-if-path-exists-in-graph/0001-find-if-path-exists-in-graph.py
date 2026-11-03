class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Determines if there exists a valid path from source to destination in an undirected graph.
      
        Args:
            n: Number of vertices in the graph (0 to n-1)
            edges: List of edges where each edge is [u, v] representing an undirected edge
            source: Starting vertex
            destination: Target vertex
          
        Returns:
            True if a path exists from source to destination, False otherwise
        """
      
        def dfs(current_node: int) -> bool:
            """
            Performs depth-first search to find if destination is reachable from current_node.
          
            Args:
                current_node: The current vertex being explored
              
            Returns:
                True if destination is reachable from current_node, False otherwise
            """
            # Base case: reached the destination
            if current_node == destination:
                return True
          
            # If node has already been visited, avoid cycles
            if current_node in visited:
                return False
          
            # Mark current node as visited
            visited.add(current_node)
          
            # Recursively explore all neighbors
            # Returns True if any neighbor leads to the destination
            return any(dfs(neighbor) for neighbor in adjacency_list[current_node])
      
        # Build adjacency list representation of the graph
        adjacency_list = [[] for _ in range(n)]
        for u, v in edges:
            adjacency_list[u].append(v)  # Add edge from u to v
            adjacency_list[v].append(u)  # Add edge from v to u (undirected graph)
      
        # Initialize set to track visited nodes
        visited = set()
      
        # Start DFS from the source node
        return dfs(source)
