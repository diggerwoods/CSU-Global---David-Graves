import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

import itertools

def calculate_shortest_route(graph, stops):
    # Generate all permutations of stops
    permutations = itertools.permutations(stops)
    best_route = None
    min_distance = float('inf')

    for route in permutations:
        total_distance = 0
        valid_route = True

        # Calculate the total distance for the current route
        for i in range(len(route) - 1):
            start, end = route[i], route[i + 1]
            if end in graph[start]:
                total_distance += graph[start][end]
            else:
                valid_route = False
                break

        # Update the best route if the current one is shorter
        if valid_route and total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    return best_route, min_distance

# Example graph with real-time traffic data (weights represent travel time in minutes)
real_time_graph = {
    'Restaurant': {'Customer1': 10, 'Customer2': 15, 'Customer3': 20},
    'Customer1': {'Customer2': 5, 'Customer3': 10, 'Restaurant': 10},
    'Customer2': {'Customer1': 5, 'Customer3': 5, 'Restaurant': 15},
    'Customer3': {'Customer1': 10, 'Customer2': 5, 'Restaurant': 20}
}

# All the customer stops
stops = ['Restaurant', 'Customer1', 'Customer2', 'Customer3']

# Calculate the best route
best_route, min_distance = calculate_shortest_route(real_time_graph, stops)

print("Best Route:", " -> ".join(best_route))
print("Minimum Distance:", min_distance, "minutes")
