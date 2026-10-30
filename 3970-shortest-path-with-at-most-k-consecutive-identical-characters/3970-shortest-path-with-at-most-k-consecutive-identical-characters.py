import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))

        # Step 2: dist[node][count] = minimum weight
        INF = 10**9
        dist = [[INF] * (k + 1) for _ in range(n)]

        minheap = []

        dist[0][1] = 0
        heapq.heappush(minheap, (0, 0, 1))  # (weight, node, count)

        # Step 3: Dijkstra
        while minheap:
            wt, u, count = heapq.heappop(minheap)

            if u == n - 1:
                return wt

            if wt > dist[u][count]:
                continue

            for v, edge_wt in adj[u]:
                next_count = count + 1 if labels[v] == labels[u] else 1

                if next_count > k:
                    continue

                next_wt = wt + edge_wt

                if next_wt < dist[v][next_count]:
                    dist[v][next_count] = next_wt
                    heapq.heappush(minheap, (next_wt, v, next_count))

        return -1