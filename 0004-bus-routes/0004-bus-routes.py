from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # If already at destination, no buses needed
        if source == target:
            return 0
      
        # Build adjacency list: stop -> list of bus indices that visit this stop
        stop_to_buses = defaultdict(list)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_index)
      
        # Check if source and target are reachable by any bus
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
      
        # BFS queue: stores (current_stop, number_of_buses_taken)
        queue = deque([(source, 0)])
      
        # Track visited buses to avoid revisiting the same bus route
        visited_buses = set()
      
        # Track visited stops to avoid revisiting the same stop
        visited_stops = {source}
      
        # BFS traversal
        while queue:
            current_stop, buses_taken = queue.popleft()
          
            # Check if we've reached the target
            if current_stop == target:
                return buses_taken
          
            # Explore all buses that visit the current stop
            for bus_index in stop_to_buses[current_stop]:
                # Skip if we've already taken this bus
                if bus_index in visited_buses:
                    continue
              
                # Mark this bus as visited
                visited_buses.add(bus_index)
              
                # Add all unvisited stops on this bus route to the queue
                for next_stop in routes[bus_index]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
      
        # Target is unreachable
        return -1
