import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Graph with real-time traffic data (weights represent travel time in minutes)
city_map = {
    'Restaurant': {'A': 5, 'B': 10},
    'A': {'Restaurant': 5, 'C': 3, 'D': 9},
    'B': {'Restaurant': 10, 'D': 2},
    'C': {'A': 3, 'D': 4},
    'D': {'A': 9, 'B': 2, 'C': 4},
}

# Imagine a food delivery app where the graph represents a city map. Nodes are locations (restaurants, delivery points, intersections), 
# and edges have weights based on real-time traffic data (e.g., travel time in minutes).

# Start from the restaurant and find the shortest path to all locations
shortest_paths = dijkstra(city_map, 'Restaurant')

# Output the shortest path to the delivery point
print("Shortest time to each location:", shortest_paths)

# If the real-time traffic data changes, the weights in the graph will adjust dynamically. For the above example, the output might look like: