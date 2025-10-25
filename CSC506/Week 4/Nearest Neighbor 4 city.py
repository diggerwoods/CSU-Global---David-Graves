import numpy as np
import time

# Starts timer for algorithm
start_time = time.time()

# Define the distance matrix for 4 cities
distances = np.array([
    [0, 557, 611, 830],  # Distances from Denver
    [557, 0, 1140, 1354],  # Distances from Kansas City
    [611, 1140, 0, 271],  # Distances from Las Vegas
    [830, 1354, 271, 0],  # Distances from Los Angeles
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

# Starting from Denver (index 0)
start_city = 0
path, total_distance = nearest_neighbor_algorithm(start_city, distances)

# Print the result
city_names = ['Denver(0)', 'Kansas City(1)', 'Las Vegas(2)', 'Los Angeles(3)']
path_names = [city_names[city] for city in path]
print(f"Path: {' -> '.join(path_names)}")
print(f"Total distance: {total_distance} miles")

# Finds the total time for algorithm and prints
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
