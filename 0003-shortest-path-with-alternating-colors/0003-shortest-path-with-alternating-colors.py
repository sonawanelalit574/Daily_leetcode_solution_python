from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # Build adjacency lists for both red and blue edges
        # graph[0] stores red edges, graph[1] stores blue edges
        graph = [defaultdict(list), defaultdict(list)]
      
        # Populate red edges (index 0)
        for source, destination in redEdges:
            graph[0][source].append(destination)
      
        # Populate blue edges (index 1)
        for source, destination in blueEdges:
            graph[1][source].append(destination)
      
        # Initialize result array with -1 (unreachable)
        shortest_distances = [-1] * n
      
        # Track visited states as (node, last_color_used)
        visited = set()
      
        # BFS queue: start from node 0 with both color options
        # (node_id, color) where color 0=red, 1=blue
        queue = deque([(0, 0), (0, 1)])
      
        # Current distance from source
        distance = 0
      
        # BFS traversal
        while queue:
            # Process all nodes at current distance level
            for _ in range(len(queue)):
                current_node, last_color = queue.popleft()
              
                # Update shortest distance if not yet set
                if shortest_distances[current_node] == -1:
                    shortest_distances[current_node] = distance
              
                # Mark this state as visited
                visited.add((current_node, last_color))
              
                # Alternate color for next edge (XOR with 1 flips 0↔1)
                next_color = last_color ^ 1
              
                # Explore neighbors using the alternating color
                for neighbor in graph[next_color][current_node]:
                    if (neighbor, next_color) not in visited:
                        queue.append((neighbor, next_color))
          
            # Increment distance for next level
            distance += 1
      
        return shortest_distances
