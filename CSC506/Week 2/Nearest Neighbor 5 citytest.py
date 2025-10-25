import numpy as np

# Example distance matrix (in kilometers)
# Cities: A, B, C, D, E, F
distances = np.array([
    [0, 10, 15, 20, 25, 30],  # Distances from city A
    [10, 0, 35, 25, 30, 20],  # Distances from city B
    [15, 35, 0, 30, 20, 25],  # Distances from city C
    [20, 25, 30, 0, 15, 10],  # Distances from city D
    [25, 30, 20, 15, 0, 35],  # Distances from city E
    [30, 20, 25, 10, 35, 0]   # Distances from city F
])

def nearest_neighbor_algorithm(start_city, distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    path = [start_city]
    total_distance = 0
    current_city = start_city
    visited[current_city] = True

    for _ in range(num_cities - 1):
        nearest_city = None
        nearest_distance = float('inf')
        for city in range(num_cities):
            if not visited[city] and distances[current_city][city] < nearest_distance:
                nearest_city = city
                nearest_distance = distances[current_city][city]
        path.append(nearest_city)
        total_distance += nearest_distance
        visited[nearest_city] = True
        current_city = nearest_city

    # Return to the starting city
    total_distance += distances[current_city][start_city]
    path.append(start_city)

    return path, total_distance

# Starting from city A (index 0)
start_city = 0
path, total_distance = nearest_neighbor_algorithm(start_city, distances)

# Print the result
city_names = ['A', 'B', 'C', 'D', 'E', 'F']
path_names = [city_names[city] for city in path]
print(f"Path: {' -> '.join(path_names)}")
print(f"Total distance: {total_distance} km")